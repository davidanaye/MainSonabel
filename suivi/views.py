from venv import logger
from django.shortcuts import render
from suivi.forms import *
from suivi.models import *
from django.contrib import messages
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from  django.views.decorators.cache import cache_control
from django.http import Http404, JsonResponse, HttpResponseRedirect, HttpResponse
from django.urls import reverse




@login_required
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def home(request):
    return render(request, 'suivi/home.html')





@login_required
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def itemsliste(request):
    # Génère une liste d'années de 2020 à 2050
    years = list(range(2020, 2051))  
    
    # Récupère tous les éléments du modèle Planitems
    planitems = Planitems.objects.all()  
    
    # Rendu du template avec les années et les éléments planitems
    return render(request, 'suivi/planitemsliste.html', {'years': years, 'planitems': planitems})





@login_required
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def addplanitems(request):
    if request.method=="POST":
        form = PlanitemsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Ajour effectué !")
            return redirect('itemsliste')
        else:
            return render(request, 'suivi/add_planitems.html', {'form': form})
    else:
        form = PlanitemsForm()
        return render(request, 'suivi/add_planitems.html', {'form': form})
    


@login_required
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def delete_planitem(request, id):
    item = Planitems.objects.get(id = id)
    item.delete()
    messages.success(request, 'supprimer avec susccès !')
    return HttpResponseRedirect(reverse("itemsliste"))




@login_required
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def dossier(request):
    if request.user.is_authenticated:
        agent = request.user

        # Récupérer toutes les années distinctes disponibles
        years = Plans.objects.all()

        # Récupérer l'année sélectionnée dans le POST, sinon prendre la dernière année
        selected_year = request.POST.get('annee')

        if not selected_year:
            # Si aucune année n'est sélectionnée, prendre l'année du dernier enregistrement dans Plans
            latest_plan = Plans.objects.latest('id')
            selected_year = latest_plan.id

        # Filtrer les éléments de plan en fonction de l'année sélectionnée et de l'agent connecté
        items = Planitems.objects.filter(agent_charge_dossier=agent, annee_id=selected_year)

        context = {
            "items": items,
            "years": years,  # Passer les années au template
            "selected_year": selected_year,
        }
        return render(request, 'suivi/dossier.html', context)

    return redirect('login')



@login_required
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def listdoc(request):
    # Check if user is authenticated
    if request.user.is_authenticated:
        # Get user authenticated
        agent = user=request.user
        # get All Dossier when user is owner
        dossiers = Dossiers.objects.filter(owner=agent)

        # Check if user have Dossier
        if dossiers.exists():
            context = {"dossiers": dossiers}
            return render(request, 'suivi/listdoc.html',context)

    return render(request, 'suivi/listdoc.html')





@login_required
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def adddossier(request, id):
    # Get a planitems objet
    plan_item = get_object_or_404(Planitems, id=id)

    if request.method == "POST":
        # Create a form
        form = DossierForm(request.POST, request.FILES)
        if form.is_valid():
            # Sauve a form
            dossier = form.save(commit=False)
            dossier.planitem_id = plan_item
            if request.user.is_authenticated:
                # Get user authenticated
                agent = user=request.user
                dossier.owner = agent
                dossier.save()
            messages.success(request, "Dossier ajouté avec succès !")
            return redirect('listdoc')

    else:
        # Initialize a form with data
        form = DossierForm(initial={'plan_item': plan_item})

    # Show a form
    return render(request, 'suivi/add_dossier.html', {'form': form})






@login_required
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def editdossier(request, dossier_id):
    # Get a planitems objet
    dossier = get_object_or_404(Dossiers, id=dossier_id)

    if request.method == "POST":
         # Create a form
        form = DossierForm(request.POST, request.FILES, instance=dossier)

        if form.is_valid():
            # Save form
            updated_dossier = form.save(commit=False)
            
            # check if user authenticated
            if request.user.is_authenticated:
                updated_dossier.owner = request.user
            
            # Save a form
            updated_dossier.save()

            messages.success(request, "Dossier modifié avec succès !")
            return redirect('listdoc')

    else:
        # Initialize a form with data
        form = DossierForm(instance=dossier)

    # Show a form
    return render(request, 'suivi/editdossier.html', {'form': form})


@login_required
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def delete_dossier(request, dossier_id):
    item = Dossiers.objects.get(id = dossier_id)
    # Check if this dossier have a lot
    if item.has_lots():
        messages.error(request, 'Ce dossier ne peut pas être supprimé car il contient des lots.')
    else:
        # Delete if any lot has not associate
        item.delete()
        messages.success(request, 'supprimer avec susccès !')
    return HttpResponseRedirect(reverse("listdoc"))



@login_required
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def list_dossier_lots(request, dossier_id):
    # Récupère l'objet Dossier correspondant à l'identifiant
    dossier = get_object_or_404(Dossiers, id=dossier_id)

    # Récupère tous les lots associés à ce dossier
    lots = Lots.objects.filter(dossier_id=dossier)

    # Préparer le contexte à passer au template
    context = {
        'dossier': dossier,
        'lots': lots
    }

    # Rendre le template avec le contexte
    return render(request, 'suivi/dossier_lots.html', context)



@login_required
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def adddlot(request, id):
    # Get a planitems objet
    dossier = get_object_or_404(Dossiers, id=id)

    if request.method == "POST":
        # Create a form
        form = LotForm(request.POST, request.FILES)
        if form.is_valid():
            # Sauve a form
            lot = form.save(commit=False)
            lot.dossier_id = dossier
            lot.save()
            messages.success(request, "Lot ajouté avec succès !")
            return redirect('dossier_lots', dossier_id=id)

    else:
        # Initialize a form with data
        form = LotForm(initial={'dossier': dossier})

    # Show a form
    return render(request, 'suivi/add_lot.html', {'form': form})




@login_required
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def editlot(request, id):
    # Récupère l'objet Lot à modifier
    lot = get_object_or_404(Lots, id=id)

    if request.method == "POST":
        # Create new form data
        form = LotForm(request.POST, request.FILES, instance=lot)

        if form.is_valid():
            # Save form
            updated_lot = form.save()
            # Get dossier id
            dossier_id = updated_lot.dossier_id.id
            # Reddirect this url
            messages.success(request, f"{updated_lot.num_lot} de {updated_lot.dossier_id.numero_doss} modifié avec succès !")
            return redirect('dossier_lots', dossier_id=dossier_id)

    else:
        # Initialize a form with data
        form = LotForm(instance=lot)

    return render(request, 'suivi/editlot.html', {'form': form, 'lot': lot})



@login_required
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def delete_lot(request, lot_id):
    # Récupère l'objet Lot à modifier
    item = get_object_or_404(Lots, id=lot_id)
    dossier_id = item.dossier_id.id
    item.delete()
    messages.success(request, 'supprimer avec susccès !')
    return HttpResponseRedirect(reverse("dossier_lots", kwargs={'dossier_id': dossier_id}))



@login_required
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def suivi(request):
    # Check if user is authenticated
    if request.user.is_authenticated:
        # Get user authenticated
        agent = user=request.user
        # get All Dossier when user is owner
        dossiers = Dossiers.objects.filter(owner=agent)
        # Maintenant, filtrer les lots associés à ces dossiers
        lots_associated = Lots.objects.filter(dossier_id__in=dossiers).count()

        # Check if user have Dossier
        if dossiers.exists():
            context = {"dossiers": dossiers, "lots_associated":lots_associated}
            return render(request, 'suivi/suivi.html',context)

    return render(request, 'suivi/suivi.html')



@login_required
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def process_dossier(request, dossier_id):
    dossier = get_object_or_404(Dossiers, id=dossier_id)

    avis = Avis.objects.filter(dossier_id=dossier.id)
    offres = Offres.objects.filter(dossier=dossier)
    resultats = Resultats.objects.filter(offre__dossier=dossier)
    marches = Marches.objects.filter(offre__dossier=dossier)  # Ajoutez marches au contexte
    context = {
        'dossier': dossier,
        'avis': avis,
        'offres': offres,
        'resultats': resultats,
        'marches': marches,
    }

    return render(request, 'suivi/process_dossier.html', context)





    



@login_required
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def addavis(request, dossier_id):
    # Get a planitems objet
    dossier = get_object_or_404(Dossiers, id=dossier_id)

    if request.method == "POST":
        # Create a form
        form = AvisForm(request.POST, request.FILES)
        if form.is_valid():
            # Sauve a form
            avis = form.save(commit=False)
            avis.dossier_id = dossier
            avis.save()
            messages.success(request, "Avis ajouté avec succès !")
            return redirect('process_dossier', dossier_id=dossier_id)

    else:
        # Initialize a form with data
        form = AvisForm(initial={'dossier': dossier})

    # Show a form
    return render(request, 'suivi/addavis.html', {'form': form, "dossier":dossier})





@login_required
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def editavis(request, avis_id):
    # Récupère l'objet Lot à modifier
    item = get_object_or_404(Avis, id=avis_id)

    if request.method == "POST":
        # Create new form data
        form = AvisForm(request.POST, request.FILES, instance=item)

        if form.is_valid():
            # Save form
            updated_avis = form.save()
            # Get dossier id
            dossier_id = updated_avis.dossier_id.id
            # Reddirect this url
            messages.success(request, " modifié avec succès !")
            return redirect('process_dossier', dossier_id=dossier_id)

    else:
        # Créer le formulaire avec les données existantes
        form = AvisForm(instance=item)
    return render(request, 'suivi/editavis.html', {'form': form, 'item': item})


@login_required
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def deleteavis(request, avis_id):
    # Récupérer l'objet Avis à supprimer
    item = get_object_or_404(Avis, id=avis_id)
    dossier_id = item.dossier_id.id  # Obtenez l'ID du dossier pour rediriger après suppression

    # Supprimer l'avis
    item.delete()
    messages.success(request, "Avis supprimé avec succès !")
    
    # Rediriger vers la liste des avis du dossier
    return redirect('process_dossier', dossier_id=dossier_id)



# @login_required
# @cache_control(no_cache=True, must_revalidate=True, no_store=True)
# def addoffre(request):
@login_required
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def addoffre(request, dossier_id):
    dossier = get_object_or_404(Dossiers, id=dossier_id)

    if request.method == "POST":
        form = OffreForm(request.POST, request.FILES, dossier=dossier)

        if form.is_valid():
            offre = form.save(commit=False)
            offre.dossier = dossier

            # Gestion du nouveau fournisseur
            entreprise_nom = form.cleaned_data.get('entreprise')
            # Créer ou obtenir le fournisseur avant de sauvegarder l'offre
            fournisseur, created = Fournisseurs.objects.get_or_create(nom_four=entreprise_nom)
            offre.entreprise = fournisseur

            offre.save()
            messages.success(request, "Offre ajoutée avec succès !")
            return redirect('process_dossier', dossier.id)
        else:
            # Si le formulaire n'est pas valide, réattribuer les entreprises disponibles
            form.fields['entreprise'].queryset = Fournisseurs.objects.all()
    else:
        form = OffreForm(dossier=dossier)

    print(f"Nombre de lots dans le formulaire : {form.fields['lot'].queryset.count()}")
    return render(request, 'suivi/editoffre.html', {'form': form, 'dossier': dossier})




@login_required
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def modifier_offres(request, dossier_id, offre_id):
    dossier = get_object_or_404(Dossiers, id=dossier_id)
    offre = get_object_or_404(Offres, id=offre_id, dossier=dossier)
    
    if request.method == 'POST':
        form = OffreForm(request.POST, instance=offre, dossier=dossier)
        if form.is_valid():
            form.save()
            messages.success(request, "Modification effectuée avec succès!")
            return redirect('process_dossier', dossier_id=dossier.id)
    else:
        form = OffreForm(instance=offre, dossier=dossier)
    
    context = {
        'form': form,
        'dossier': dossier,
        'offre': offre
    }
    return render(request, 'suivi/modifier_offres.html', context)



@login_required
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def editplanitems(request, id):
    item = Planitems.objects.get(id=id)
    if request.method == 'POST':
        form = PlanitemsForm(request.POST, instance=item)
        if form.is_valid():
            form.save(id)
            messages.success(request, "Modification effectué avec susccès!")
            return redirect('itemsliste')
    else:
        form = PlanitemsForm(instance=item)
    return render(request, 'suivi/edit_planitems.html', {'item':item, 'form':form})


@login_required
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def itemsoffres(request, dossier_id):
    dossier = get_object_or_404(Dossiers, id=dossier_id)
    offres = Offres.objects.filter(dossier=dossier)
    context = {
        'dossier': dossier,
        'offres': offres
    }
    return render(request, 'suivi/offre.html', context)


@login_required
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def supprimer_offres(request, dossier_id, offre_id):
    offre = get_object_or_404(Offres, id=offre_id, dossier_id=dossier_id)
    if request.method == 'POST':
        offre.delete()
        messages.success(request, "Offre supprimée avec succès!")
        return redirect('process_dossier', dossier_id=dossier_id)
    
    context = {
        'dossier_id': dossier_id,
        'offre': offre
    }
    return render(request, 'suivi/supprimer_offres.html', context)

@login_required
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def addresultat(request, offre_id):
    offre = get_object_or_404(Offres, id=offre_id)
    dossier = offre.dossier

    if request.method == "POST":
        form = ResultatsForm(request.POST, request.FILES)  # Inclure request.FILES pour les fichiers
        if form.is_valid():
            # Vérifier si un résultat pour cette offre existe déjà
            if Resultats.objects.filter(offre=offre).exists():
                messages.error(request, "Un résultat existe déjà pour cette offre.")
                return redirect('process_dossier', dossier.id)

            resultat = form.save(commit=False)
            resultat.offre = offre
            resultat.dossier_id = dossier.id
            resultat.lot = offre.lot
            resultat.save()
            messages.success(request, "Analyse bien effectuée !")
            return redirect('process_dossier', dossier.id)
        else:
            messages.error(request, "Erreur lors de la soumission du formulaire.")
    else:
        form = ResultatsForm()

    attributaires = Offres.objects.values_list('entreprise', 'id')
    return render(request, 'suivi/editresultat.html', {'form': form, 'dossier': dossier, 'attributaires': attributaires})


import logging
@login_required
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def addmarche(request, dossier_id):
    dossier = get_object_or_404(Dossiers, id=dossier_id)
    logger.debug(f"Recherche du dossier avec l'ID: {dossier_id}")

    if request.method == "POST":
        form = MarcheForm(request.POST)
        if form.is_valid():
            marche = form.save(commit=False)
            marche.dossier = dossier

            # Associer l'attributaire depuis le modèle Resultats
            resultat = Resultats.objects.filter(offre=marche.offre).first()
            if resultat and resultat.attributaire:
                marche.attributaire = resultat.attributaire

            marche.save()
            messages.success(request, "Marché ajouté avec succès !")
            return redirect('process_dossier', dossier.id)
        else:
            messages.error(request, "Erreur lors de l'ajout du marché. Veuillez vérifier les informations fournies.")
    else:
        offres = Offres.objects.filter(dossier=dossier)
        form = MarcheForm()
        form.fields['offre'].queryset = offres

    return render(request, 'suivi/editMarche.html', {'form': form, 'dossier': dossier})





@login_required
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def supprimer_resultat(request, dossier_id, resultat_id):
    resultat = get_object_or_404(Resultats, id=resultat_id, offre__dossier_id=dossier_id)
    if request.method == 'POST':
        resultat.delete()
        messages.success(request, "Résultat supprimé avec succès!")
        return redirect('process_dossier', dossier_id=dossier_id)
    
    context = {
        'dossier_id': dossier_id,
        'resultat': resultat
    }

@login_required
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def supprimer_marche(request, dossier_id, marche_id):
    marche = get_object_or_404(Marches, id=marche_id, offre__dossier_id=dossier_id)
    if request.method == 'POST':
        marche.delete()
        messages.success(request, "Marché supprimé avec succès!")
        return redirect('process_dossier', dossier_id=dossier_id)
    
    context = {
        'dossier_id': dossier_id,
        'marche': marche
    }
    return render(request, 'suivi/supprimer_marche.html', context)


@login_required
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def modifier_marche(request, dossier_id, marche_id):
    dossier = get_object_or_404(Dossiers, id=dossier_id)
    marche = get_object_or_404(Marches, id=marche_id, offre__dossier=dossier)
    
    print(dossier)  # Débogage
    print(marche)   # Débogage
    
    if request.method == 'POST':
        form = MarcheForm(request.POST, instance=marche)
        if form.is_valid():
            form.save()
            messages.success(request, "Modification effectuée avec succès!")
            return redirect('process_dossier', dossier_id=dossier.id)
    else:
        form = MarcheForm(instance=marche)
    
    context = {
        'form': form,
        'dossier': dossier,
        'marche': marche
    }
    return render(request, 'suivi/modifier_marche.html', context)

@login_required
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def modifier_resultat(request, dossier_id, resultat_id):
    dossier = get_object_or_404(Dossiers, id=dossier_id)
    resultat = get_object_or_404(Resultats, id=resultat_id, offre__dossier=dossier)
    
    if request.method == 'POST':
        form = ResultatsForm(request.POST, instance=resultat)
        if form.is_valid():
            form.save()
            messages.success(request, "Modification effectuée avec succès!")
            return redirect('process_dossier', dossier_id=dossier.id)
    else:
        form = ResultatsForm(instance=resultat)
    
    context = {
        'form': form,
        'dossier': dossier,
        'resultat': resultat
    }
    return render(request, 'suivi/modifier_resultat.html', context)

@login_required
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def etat_dossiers(request):
    dossiers = Dossiers.objects.all()
    dossiers_info = []
    
    plan = Plans.objects.first()

    def calculate_progress(dossier_info):
        fields = [
            dossier_info['ref_dossier'],
            dossier_info['ref_pub'],
            dossier_info['date_publi'],
            dossier_info['nom_attributaire'],
            dossier_info['contagieux_litige'],
            dossier_info['numero_marche'],
            dossier_info['date_lancement_publication'],
            dossier_info['date_notif_projet_contrat'],
            dossier_info['date_sign_contrat'],
            dossier_info['montant']
        ]
        total_fields = len(fields)
        filled_fields = sum(1 for field in fields if field is not None)
        return round((filled_fields / total_fields) * 100, 2)

    for dossier in dossiers:
        # Vérification de l'étape Avis de Publication
        avis_list = Avis.objects.filter(dossier_id=dossier.id)
        ref_pub, date_lancement_publication, date_publi = None, None, None
        for avis in avis_list:
            if avis.num_publi and avis.date_publi:  # Vérifiez que la ligne est valide
                ref_pub = avis.num_publi
                date_lancement_publication = avis.date_lancement_pulication
                date_publi = avis.date_publi
                break  # Utilise la première ligne valide trouvée

        # Vérification de l'étape Résultats
        results_list = Resultats.objects.filter(dossier_id=dossier.id)
        nom_attributaire, contagieux_litige = None, None
        for resultat in results_list:
            if resultat.attributaire:  # Vérifiez que la ligne est valide
                nom_attributaire = resultat.attributaire
                contagieux_litige = resultat.litige
                break  # Utilise la première ligne valide trouvée

        # Vérification de l'étape Marché
        marches_list = Marches.objects.filter(offre__dossier=dossier)
        numero_marche, montant, date_notif_projet_contrat, date_sign_contrat = None, None, None, None

        for marche in marches_list:
            # Vérifiez que la ligne est valide et que les champs ne sont pas vides ou null
            if marche.num_ref and marche.montant and marche.date_notif and marche.date_retour_sign:
                numero_marche = marche.num_ref
                montant = marche.montant
                date_notif_projet_contrat = marche.date_notif
                date_sign_contrat = marche.date_retour_sign
                break  # Utilise la première ligne valide trouvée

        # Calcul de la progression et de l'état
        dossier_info = {
            'ref_dossier': dossier.numero_doss,
            'intitule_dossier': dossier.intitule_doss,
            'date_publi': date_publi,
            'date_lancement_publication': date_lancement_publication,
            'montant': montant,
            'ref_pub': ref_pub,
            'nom_attributaire': nom_attributaire,
            'contagieux_litige': contagieux_litige,
            'numero_marche': numero_marche,
            'date_notif_projet_contrat': date_notif_projet_contrat,
            'date_sign_contrat': date_sign_contrat,
            'progression': 0,
            'etat': "Non entamé"
        }

        dossier_info['progression'] = calculate_progress(dossier_info)

        # Déterminer l'état basé sur les informations disponibles
        if dossier_info['date_lancement_publication'] and dossier_info['ref_pub'] and dossier_info['date_publi'] and dossier_info['nom_attributaire']:
            if dossier_info['contagieux_litige'] and dossier_info['montant'] and dossier_info['numero_marche'] and dossier_info['date_sign_contrat'] and dossier_info['date_notif_projet_contrat']:
                dossier_info['etat'] = "En cours d'exécution"
                dossier_info['progression'] = 100
            else:
                dossier_info['etat'] = "Lancé non attribué"
        else:
            dossier_info['etat'] = "Non entamé"

        dossiers_info.append(dossier_info)

    # Calculer les statistiques globales
    total_dossiers = len(dossiers_info)
    en_cours = sum(1 for d in dossiers_info if d['etat'] == "En cours d'exécution")
    non_entame = sum(1 for d in dossiers_info if d['etat'] == "Non entamé")
    lance_non_attribue = sum(1 for d in dossiers_info if d['etat'] == "Lancé non attribué")

    stats = {
        'global_en_cours': round((en_cours / total_dossiers) * 100, 2) if total_dossiers else 0,
        'global_non_entame': round((non_entame / total_dossiers) * 100, 2) if total_dossiers else 0,
        'global_lance_non_attribue': round((lance_non_attribue / total_dossiers) * 100, 2) if total_dossiers else 0,
        'moyenne_totale': round((sum(d['progression'] for d in dossiers_info) / total_dossiers), 2) if total_dossiers else 0
    }

    context = {
        'dossiers_info': dossiers_info,
        'stats': stats,
        'plan': plan,
    }

    return render(request, 'suivi/etat.html', context)

from django.views.decorators.csrf import csrf_exempt

@login_required
@csrf_exempt  # Permet d'éviter les problèmes CSRF pour l'appel AJAX
def add_new_entreprise(request):
    if request.method == "POST":
        entreprise_nom = request.POST.get('entreprise_nom', '')
        if entreprise_nom:
            fournisseur, created = Fournisseurs.objects.get_or_create(nom_four=entreprise_nom)
            return JsonResponse({'success': True, 'id': fournisseur.id, 'nom_four': fournisseur.nom_four})
    return JsonResponse({'success': False})


from django.http import JsonResponse

@login_required
def get_attributaire(request):
    offre_id = request.GET.get('offre_id')
    try:
        # Récupérer l'offre sélectionnée
        offre = Offres.objects.get(pk=offre_id)
        # Assurez-vous que le résultat est relié correctement et a un attributaire
        attributaire_id = offre.resultat.attributaire.id if offre.resultat and offre.resultat.attributaire else None
        return JsonResponse({'attributaire_id': attributaire_id})
    except Offres.DoesNotExist:
        return JsonResponse({'attributaire_id': None})
    
import csv
import chardet

@login_required
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def import_plan(request):
    if request.method == 'POST':
        annee_value = request.POST.get('annee')
        csv_file = request.FILES.get('csv_file')

        if not csv_file:
            messages.error(request, 'Veuillez sélectionner un fichier CSV à télécharger.')
            return redirect('itemsliste')

        if not csv_file.name.endswith('.csv'):
            messages.error(request, 'Ce fichier n\'est pas un fichier CSV')
            return redirect('itemsliste')

        try:
            # Détection automatique de l'encodage
            raw_data = csv_file.read()
            result = chardet.detect(raw_data)
            encoding = result['encoding']
            decoded_file = raw_data.decode(encoding).splitlines()

            csv_reader = csv.DictReader(decoded_file, delimiter=';')

            successfully_imported = 0

            plan, created = Plans.objects.get_or_create(annee=annee_value)

            for row in csv_reader:
                # Debugging: Afficher les clés et les données de la ligne
                print(f"Row keys: {row.keys()}")
                print(f"Row data: {row}")

                agent_id_str = row.get('agent_id', '')
                if agent_id_str:
                    try:
                        agent_id = int(agent_id_str)
                        agent = User.objects.get(id=agent_id)
                    except (ValueError, User.DoesNotExist):
                        agent = None
                else:
                    agent = None

                # Map fields from the CSV to the model fields
                planitem_data = {
                    'num_ordre': row.get('num_ordre', None),
                    'num_credit': row.get('credit', None),
                    'budget': row.get('budget', None),
                    'direction_charge_dossier': row.get('localisation', None),
                    'unite_service_beneficiaire': row.get('centre_cout', None),
                    'montant_inscription_budgetaire': row.get('montant_dispo', None),
                    'montant_depenses_engagees_non_liquidees': row.get('montant_estime', None),
                    'disponible': row.get('montant_dispo', None),
                    'elements_composantes': row.get('composante', None),
                    'type_prestation': row.get('type', None),
                    'nature_prestations': row.get('designation', None),
                    'mode_passation': row.get('mode', None),
                    'agent_charge_dossier': agent,
                    'date_prevue_reception_dossier_technique': row.get('date_tech', None),
                    'date_reelle_reception_dossier_technique': row.get('date_tech_reel', None),
                    'service_charge_dossier_technique': row.get('localisation', None),
                    'intitule_dossier': row.get('designation', None),
                    'ref_dossier_appel_concurrence': row.get('ref_dossier_appel_concurrence', None),
                    'dossiers_non_recus_montant_alloue': row.get('dossiers_non_recus_montant_alloue', None),
                    'taux_reception_dossiers_dmp': row.get('taux_reception_dossiers_dmp', None),
                    'nombre_dossiers_recus': row.get('nombre_dossiers_recus', None),
                    'date_transmission_signature': row.get('date_transmission_signature', None),
                    'date_retour_signature': row.get('date_retour_signature', None),
                    'date_transmission_par_dgcmef': row.get('date_dgcmef', None),
                    'date_prevue_lancement_dgcmef': row.get('date_prevue_lancement_dgcmef', None),
                    'date_reelle_lancement_dgcmef': row.get('date_reelle_lancement_dgcmef', None),
                    'dossiers_non_lances_montant_alloue': row.get('dossiers_non_lances_montant_alloue', None),
                    'taux_lancement_dossiers': row.get('taux_lancement_dossiers', None),
                    'nombre_dossiers_lances': row.get('nombre_dossiers_lances', None),
                    'date_prevue_remise_offres': row.get('date_off', None),
                    'date_reelle_remise_offres': row.get('date_off_reel', None),
                    'convocation_ouverture': row.get('convocation_ouverture', None),
                    'transmission_pv_signature': row.get('transmission_pv_signature', None),
                    'retour_signature_pv': row.get('retour_signature_pv', None),
                    'transmission_dgcmef_eventuel': row.get('transmission_dgcmef_eventuel', None),
                    'temps_necessaire_evaluation_offres_jours': row.get('temp', None),
                    'convocation_analyses_offres': row.get('convocation_analyses_offres', None),
                    'date_effectives_analyses_offres': row.get('date_effectives_analyses_offres', None),
                    'duree_reelle_evaluation_offres_jours': row.get('temp_reel', None),
                    'date_introduction_signature': row.get('date_introduction_signature', None),
                    'date_retour_signature_dg': row.get('date_retour_signature_dg', None),
                    'date_transmission_dgcmef': row.get('date_transmission_dgcmef', None),
                    'observations_eventuelles_dgcmef': row.get('observations_eventuelles_dgcmef', None),
                    'reference_publication': row.get('reference_publication', None),
                    'publication_dgcmef': row.get('publication_dgcmef', None),
                    'nom_attributaire_provisoire': row.get('nom_attributaire_provisoire', None),
                    'contentieux_litiges': row.get('contentieux_litiges', None),
                    'montant': row.get('montant_dispo', None),
                    'numero_marche': row.get('numero_marche', None),
                    'date_notification_projet_contrat': row.get('date_notification_projet_contrat', None),
                    'date_signature_contrat': row.get('date_signature_contrat', None),
                    'dossiers_marches_non_conclu_montant_alloue': row.get('dossiers_marches_non_conclu_montant_alloue', None),
                    'taux_passation_marches': row.get('taux_passation_marches', None),
                    'nombre_marches_conclure_par_ligne_ppm': row.get('nombre_marches_conclure_par_ligne_ppm', None),
                    'nombre_marches_conclus_par_ligne_ppm': row.get('nombre_marches_conclus_par_ligne_ppm', None),
                    'nombre_ligne_fait_objet_marche': row.get('nombre_ligne_fait_objet_marche', None),
                    'date_remise_garantie_bonne_execution': row.get('date_remise_garantie_bonne_execution', None),
                    'date_transmission_contrat_enregistrement': row.get('date_transmission_contrat_enregistrement', None),
                    'date_retour_enregistrement_contrat': row.get('date_retour_enregistrement_contrat', None),
                    'date_emission_ordre_service': row.get('date_emission_ordre_service', None),
                    'date_remise_site': row.get('date_remise_site', None),
                    'date_demarrage_prevue_execution': row.get('date_demarrage', None),
                    'date_reelle_demarrage_execution': row.get('date_reel_demarrage', None),
                    'delai_prevue_execution': row.get('delai_exe', None),
                    'delai_reelle_execution': row.get('delai_reel_exe', None),
                    'date_butoir': row.get('date_butoir', None),
                    'gestionnaire_credit': row.get('gestionnaire_credit', None),
                    'date_reelle_lancement': row.get('date_reelle_lancement', None),
                    'execution_ppm_2023_30_septembre': row.get('execution_ppm_2023_30_septembre', None),
                    'observations_suivi_quotidien_04_12_2023': row.get('observations_suivi_quotidien_04_12_2023', None),
                    'dossiers_recus': row.get('dossiers_recus', None),
                    'marches_en_cours_execution': row.get('marches_en_cours_execution', None),
                    'marches_executes': row.get('marches_executes', None),
                    'types': row.get('types', None),
                    'observations': row.get('observation', None),
                }

                print(f"Creating Planitems with data: {planitem_data}")  # Debug print statement

                Planitems.objects.create(
                    annee=plan,
                    **planitem_data
                )

                successfully_imported += 1

            messages.success(request, f"{successfully_imported} plan(s) ont été importés avec succès.")
            return redirect('itemsliste')
        except Exception as e:
            print(f'Erreur lors de l\'importation des données : {str(e)}')
            messages.error(request, f'Erreur lors de l\'importation des données : {str(e)}')
            return redirect('itemsliste')
    else:
        return render(request, 'suivi/planitemsliste.html')


    

@login_required
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def filter_plan(request):
    # Récupérer toutes les années distinctes disponibles
    years = Plans.objects.all()
    
    # Récupérer l'année sélectionnée dans le POST, sinon prendre la dernière année
    selected_year = request.POST.get('annee')
    
    if not selected_year:
        # Si aucune année n'est sélectionnée, prendre l'année du dernier enregistrement dans Plans
        latest_plan = Plans.objects.latest('id')
        selected_year = latest_plan.id
    
    # Filtrer les éléments de plan en fonction de l'année sélectionnée
    planitems = Planitems.objects.filter(annee_id=selected_year)

    # Rendre le template avec les éléments filtrés
    return render(request, 'suivi/planitemsliste.html', {
        'planitems': planitems,
        'years': years,
        'selected_year': selected_year
    })
    
@login_required
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def ppm_view(request, plan_id):
    # Récupérer tous les éléments du modèle Planitems avec les relations nécessaires
    planitems = Planitems.objects.select_related(
        'annee', 'agent_id'
    ).all()

    planitems_data = []

    def calculate_progress(dossier_info):
        fields = [
            dossier_info['ref_dossier'],
            dossier_info['ref_pub'],
            dossier_info['date_publi'],
            dossier_info['nom_attributaire'],
            dossier_info['contagieux_litige'],
            dossier_info['numero_marche'],
            dossier_info['date_lancement_publication'],
            dossier_info['date_notif_projet_contrat'],
            dossier_info['date_sign_contrat'],
            dossier_info['montant']
        ]
        total_fields = len(fields)
        filled_fields = sum(1 for field in fields if field is not None)
        return round((filled_fields / total_fields) * 100, 2)

    for item in planitems:
        dossier = Dossiers.objects.filter(planitem_id=item).first()
        avis = dossier.avis_set.first() if dossier else None
        resultat = Resultats.objects.filter(dossier_id=dossier.id).first() if dossier else None
        marche = Marches.objects.filter(offre__dossier=dossier).first() if dossier else None

        dossier_info = {
            'ref_dossier': dossier.numero_doss if dossier else None,
            'intitule_dossier': dossier.intitule_doss if dossier else None,
            'date_publi': avis.date_publi if avis else None,
            'date_lancement_publication': avis.date_lancement_pulication if avis else None,
            'montant': marche.montant if marche else None,
            'ref_pub': avis.num_publi if avis else None,
            'nom_attributaire': resultat.attributaire if resultat else None,
            'contagieux_litige': resultat.litige if resultat else None,
            'numero_marche': marche.num_ref if marche else None,
            'date_notif_projet_contrat': marche.date_notif if marche else None,
            'date_sign_contrat': marche.date_retour_sign if marche else None,
            'progression': 0,
            'etat': "Non entamé"  # Ajoutez ceci pour assurer qu'un état initial est toujours défini
        }

        dossier_info['progression'] = calculate_progress(dossier_info)

        if dossier_info['date_lancement_publication'] and dossier_info['ref_pub'] and dossier_info['date_publi'] and dossier_info['nom_attributaire']:
            if dossier_info['contagieux_litige'] and dossier_info['montant'] and dossier_info['numero_marche'] and dossier_info['date_sign_contrat'] and dossier_info['date_notif_projet_contrat']:
                dossier_info['etat'] = "En cours d'exécution"
                dossier_info['progression'] = 100
            else:
                dossier_info['etat'] = "Lancé non attribué"
        else:
            dossier_info['etat'] = "Non entamé"

        # Ajoutez l'état aux observations
        dossier_info['observations'] = dossier_info['etat']

        planitems_data.append({
            'item': item,
            'dossier_info': dossier_info,
            'avis': avis,
            'resultat': resultat,
            'marche': marche
        })

    # Rendre le template avec les éléments planitems_data
    return render(request, 'suivi/ppm.html', {'planitems_data': planitems_data})
