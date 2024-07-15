from django.db import models


class Agents(models.Model):
    nom_prenom = models.CharField(blank=True, null=True)
    telephone = models.CharField(blank=True, null=True)
    email = models.CharField(blank=True, null=True)
    fonction = models.CharField(blank=True, null=True)
    service = models.CharField(blank=True, null=True)
    localisation_id = models.IntegerField(blank=True, null=True)
    distinction = models.CharField(blank=True, null=True)
    signat = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)




class Analyses(models.Model):
    dossier_id = models.IntegerField(blank=True, null=True)
    date_convocation = models.CharField(blank=True, null=True)
    date_effec_ana = models.CharField(blank=True, null=True)
    date_trans_dgcmef = models.CharField(blank=True, null=True)
    observation = models.CharField(blank=True, null=True)
    rapport = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)



class Avenants(models.Model):
    marche_id = models.IntegerField(blank=True, null=True)
    nature_avenant = models.CharField(blank=True, null=True)
    montant = models.IntegerField(blank=True, null=True)
    date_avenant = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)




class Avis(models.Model):
    num_publi = models.CharField(blank=True, null=True)
    date_envoi = models.CharField(blank=True, null=True)
    date_publi = models.CharField(blank=True, null=True)
    fichier = models.CharField(blank=True, null=True)
    dossier_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)



class Budgets(models.Model):
    libelle = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True,blank=True, null=True)
    updated_at = models.DateTimeField(auto_now_add=True,blank=True, null=True)
    
    def __str__(self):
        return self.libelle




class Caisses(models.Model):
    num_recu = models.CharField(blank=True, null=True)
    date_recu = models.CharField(blank=True, null=True)
    vente_id = models.IntegerField(blank=True, null=True)
    modepaiement_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    ref_virement = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)




class Caminvs(models.Model):
    dossier_id = models.IntegerField(blank=True, null=True)
    date_cam = models.CharField(blank=True, null=True)
    heure_cam = models.CharField(blank=True, null=True)
    lieu_cam = models.CharField(blank=True, null=True)
    membre_cam = models.CharField(blank=True, null=True)
    membre2_cam = models.CharField(blank=True, null=True)
    membre3_cam = models.CharField(blank=True, null=True)
    membre4_cam = models.CharField(blank=True, null=True)
    membre5_cam = models.CharField(blank=True, null=True)
    ampliation = models.CharField(blank=True, null=True)
    president_cam = models.CharField(blank=True, null=True)
    distinc_presi_cam = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)



class Cautions(models.Model):
    cau_doss_id = models.IntegerField(blank=True, null=True)
    lot_id = models.IntegerField(blank=True, null=True)
    soumissionaire = models.IntegerField(blank=True, null=True)
    date_caution = models.CharField(blank=True, null=True)
    banque = models.CharField(blank=True, null=True)
    montant_caution = models.CharField(blank=True, null=True)
    caution = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)




class Cotations(models.Model):
    num_cotation = models.CharField(blank=True, null=True)
    ref_cotation = models.CharField(blank=True, null=True)
    doss_cotation_id = models.IntegerField(blank=True, null=True)
    fournisseur_id = models.IntegerField(blank=True, null=True)
    objet = models.CharField(blank=True, null=True)
    date_depot = models.CharField(blank=True, null=True)
    heure_depot = models.CharField(blank=True, null=True)
    fct_signataire = models.CharField(blank=True, null=True)
    nom_signataire = models.CharField(blank=True, null=True)
    dist_signataire = models.CharField(blank=True, null=True)
    demande_cotation = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)





class Credits(models.Model):
    libelle = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)




class Deliberations(models.Model):
    dossier_id = models.IntegerField(blank=True, null=True)
    date_convocation = models.CharField(blank=True, null=True)
    date_transpv_sign = models.CharField(blank=True, null=True)
    date_retourpv_sign = models.CharField(blank=True, null=True)
    date_transpv_dgcmef = models.CharField(blank=True, null=True)
    pvdeliberation = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)




class Devises(models.Model):
    libelle = models.CharField(blank=True, null=True)
    symbole = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)




class Dossiers(models.Model):
    planitem_id = models.IntegerField(blank=True, null=True)
    numero_doss = models.CharField(blank=True, null=True)
    intitule_doss = models.CharField(blank=True, null=True)
    date_trans_sign = models.CharField(blank=True, null=True)
    date_retour_sign = models.CharField(blank=True, null=True)
    date_trans_dgcmef = models.CharField(blank=True, null=True)
    taux_reception = models.CharField(blank=True, null=True)
    niveau_traitement = models.CharField(blank=True, null=True)
    taux_avencement = models.CharField(blank=True, null=True)
    dossier = models.CharField(blank=True, null=True)
    statut = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)



class Dossiertechs(models.Model):
    planitem_id = models.IntegerField(blank=True, null=True)
    date_tech_reel = models.CharField(blank=True, null=True)
    service = models.CharField(blank=True, null=True)
    dossiertech = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)



 


class Fournisseurs(models.Model):
    nom_four = models.CharField(blank=True, null=True)
    rccm = models.CharField(blank=True, null=True)
    ifu = models.CharField(blank=True, null=True)
    telephone1 = models.CharField(blank=True, null=True)
    telephone2 = models.CharField(blank=True, null=True)
    adresse = models.CharField(blank=True, null=True)
    email = models.CharField(blank=True, null=True)
    domaine = models.CharField(blank=True, null=True)
    type = models.CharField(blank=True, null=True)
    select = models.IntegerField(blank=True, null=True)
    chef = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)




class Immobilisations(models.Model):
    libelle = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)





class Localisations(models.Model):
    sigle = models.CharField(blank=True, null=True)
    libelle = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)





class Lots(models.Model):
    dossier_id = models.IntegerField(blank=True, null=True)
    num_lot = models.CharField(blank=True, null=True)
    intitule_lot = models.CharField(blank=True, null=True)
    montant_lot = models.IntegerField(blank=True, null=True)
    montant_vente = models.IntegerField(blank=True, null=True)
    statut = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)




class Marches(models.Model):
    mar_doss_id = models.IntegerField(blank=True, null=True)
    lot_id = models.IntegerField(blank=True, null=True)
    num_ref = models.CharField(blank=True, null=True)
    objet = models.CharField(blank=True, null=True)
    date_appro = models.CharField(blank=True, null=True)
    date_notif = models.CharField(blank=True, null=True)
    montant = models.IntegerField(blank=True, null=True)
    devise = models.CharField(blank=True, null=True)
    taxe = models.CharField(blank=True, null=True)
    montant2 = models.IntegerField(blank=True, null=True)
    devise2 = models.CharField(blank=True, null=True)
    taxe2 = models.CharField(blank=True, null=True)
    montant3 = models.IntegerField(blank=True, null=True)
    devise3 = models.CharField(blank=True, null=True)
    taxe3 = models.CharField(blank=True, null=True)
    montant4 = models.IntegerField(blank=True, null=True)
    devise4 = models.CharField(blank=True, null=True)
    taxe4 = models.CharField(blank=True, null=True)
    montant_total = models.IntegerField(blank=True, null=True)
    devise_total = models.CharField(blank=True, null=True)
    taxe_total = models.CharField(blank=True, null=True)
    delai = models.CharField(blank=True, null=True)
    attributaire = models.IntegerField(blank=True, null=True)
    date_rem_sign = models.CharField(blank=True, null=True)
    date_retour_sign = models.CharField(blank=True, null=True)
    date_rem_enr = models.CharField(blank=True, null=True)
    date_retour_enr = models.CharField(blank=True, null=True)
    marche = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)




class Modepaiements(models.Model):
    libelle = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)




class Modes(models.Model):
    libelle = models.CharField(blank=True, null=True)
    description = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)




class Offres(models.Model):
    updated_at = models.DateTimeField(blank=True, null=True)
    off_doss_id = models.IntegerField(blank=True, null=True)
    lot_id = models.IntegerField(blank=True, null=True)
    entreprise_cons = models.IntegerField(blank=True, null=True)
    date_depot = models.CharField(blank=True, null=True)
    heure_depot = models.CharField(blank=True, null=True)
    nom_prenom_dep = models.CharField(blank=True, null=True)
    telephone_dep = models.CharField(blank=True, null=True)
    montant = models.IntegerField(blank=True, null=True)
    montant_corr = models.IntegerField(blank=True, null=True)
    devise = models.CharField(blank=True, null=True)
    taxe = models.CharField(blank=True, null=True)
    montant2 = models.IntegerField(blank=True, null=True)
    montant2_corr = models.IntegerField(blank=True, null=True)
    devise2 = models.CharField(blank=True, null=True)
    taxe2 = models.CharField(blank=True, null=True)
    montant3 = models.IntegerField(blank=True, null=True)
    montant3_corr = models.IntegerField(blank=True, null=True)
    devise3 = models.CharField(blank=True, null=True)
    taxe3 = models.CharField(blank=True, null=True)
    montant4 = models.IntegerField(blank=True, null=True)
    montant4_corr = models.IntegerField(blank=True, null=True)
    devise4 = models.CharField(blank=True, null=True)
    taxe4 = models.CharField(blank=True, null=True)
    montant_offre = models.IntegerField(blank=True, null=True)
    montant_corrige = models.IntegerField(blank=True, null=True)
    devise_offre = models.CharField(blank=True, null=True)
    taxe_offre = models.CharField(blank=True, null=True)
    aucun_pli = models.IntegerField(blank=True, null=True)
    asf = models.IntegerField(blank=True, null=True)
    asc = models.IntegerField(blank=True, null=True)
    ajt = models.IntegerField(blank=True, null=True)
    drtss = models.IntegerField(blank=True, null=True)
    rccm = models.IntegerField(blank=True, null=True)
    cnf = models.IntegerField(blank=True, null=True)
    caut = models.IntegerField(blank=True, null=True)
    fichier_caution = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)




class Ordreservs(models.Model):
    marche_id = models.IntegerField(blank=True, null=True)
    ref = models.CharField(blank=True, null=True)
    date_notif = models.CharField(blank=True, null=True)
    date_debut = models.CharField(blank=True, null=True)
    ordre = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)


class Plans(models.Model):
    annee = models.IntegerField(blank=True, null=True)
    date_plan = models.DateField(blank=True, null=True)
    statut = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True,blank=True, null=True)
    updated_at = models.DateTimeField(auto_now_add=True,blank=True, null=True)
    
    def __str__(self):
        return str(self.annee)
    
    

class Planitems(models.Model):
    num_ordre = models.IntegerField(blank=True, null=True)
    plan_id = models.ForeignKey(Plans, blank=True, null=True, on_delete=models.CASCADE)
    budget = models.ForeignKey(Budgets, blank=True, null=True, on_delete=models.CASCADE)
    typcredit = models.CharField(blank=True, null=True)
    immobilisation = models.CharField(blank=True, null=True)
    credit = models.CharField(blank=True, null=True)
    centre_cout = models.CharField(blank=True, null=True)
    projet = models.CharField(blank=True, null=True)
    localisation = models.CharField(blank=True, null=True)
    responsable = models.CharField(blank=True, null=True)
    montant_estime = models.IntegerField(blank=True, null=True)
    composante = models.CharField(blank=True, null=True)
    montant_dispo = models.IntegerField(blank=True, null=True)
    designation = models.CharField(blank=True, null=True)
    type = models.CharField(blank=True, null=True)
    mode = models.CharField(blank=True, null=True)
    nbr_lot = models.CharField(blank=True, null=True)
    agent_id = models.IntegerField(blank=True, null=True)
    date_tech = models.CharField(blank=True, null=True)
    date_tech_reel = models.CharField(blank=True, null=True)
    date_dgcmef = models.CharField(blank=True, null=True)
    date_dgcmef_reel = models.CharField(blank=True, null=True)
    date_off = models.CharField(blank=True, null=True)
    date_off_reel = models.CharField(blank=True, null=True)
    temp = models.IntegerField(blank=True, null=True)
    temp_reel = models.IntegerField(blank=True, null=True)
    date_resultat = models.CharField(blank=True, null=True)
    resultat = models.CharField(blank=True, null=True)
    date_visite_site = models.CharField(blank=True, null=True)
    date_demarrage = models.CharField(blank=True, null=True)
    date_reel_demarrage = models.CharField(blank=True, null=True)
    delai_exe = models.IntegerField(blank=True, null=True)
    delai_reel_exe = models.IntegerField(blank=True, null=True)
    date_butoir = models.CharField(blank=True, null=True)
    date_reel_fin = models.CharField(blank=True, null=True)
    budget_travaux = models.CharField(blank=True, null=True)
    observation = models.CharField(blank=True, null=True)
    statut = models.CharField(blank=True, null=True)
    num_doss = models.CharField(blank=True, null=True)
    intitule_doss = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return str(self.num_ordre)








class Proceverbs(models.Model):
    dossier_id = models.IntegerField(blank=True, null=True)
    date_convocation = models.CharField(blank=True, null=True)
    date_transpv_sign = models.CharField(blank=True, null=True)
    date_retourpv_sign = models.CharField(blank=True, null=True)
    date_transpv_dgcmef = models.CharField(blank=True, null=True)
    pv = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)




class Pubavis(models.Model):
    date_bordereau = models.CharField(blank=True, null=True)
    fichier = models.CharField(blank=True, null=True)
    observation = models.CharField(blank=True, null=True)
    dossier_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)




class Resultats(models.Model):
    dossier_id = models.IntegerField(blank=True, null=True)
    date_par_res = models.CharField(blank=True, null=True)
    num_par_res = models.CharField(blank=True, null=True)
    attributaire = models.CharField(blank=True, null=True)
    litige = models.CharField(blank=True, null=True)
    fichierpub = models.CharField(blank=True, null=True)
    fichierlitige = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)




class Scaminvs(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    dossier_id = models.IntegerField(blank=True, null=True)
    date_scam = models.CharField(blank=True, null=True)
    membre4_scam = models.CharField(blank=True, null=True)
    membre5_scam = models.CharField(blank=True, null=True)
    distinc_presi_sct = models.CharField(blank=True, null=True)
    membre2_scam = models.CharField(blank=True, null=True)
    membre3_scam = models.CharField(blank=True, null=True)
    president_sct = models.CharField(blank=True, null=True)
    heure_scam = models.CharField(blank=True, null=True)
    lieu_scam = models.CharField(blank=True, null=True)
    membre_scam = models.CharField(blank=True, null=True)
    ampliation = models.CharField(blank=True, null=True)



class Typcredits(models.Model):
    libelle = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)




class Types(models.Model):
    libelle = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)




class Typreceptions(models.Model):
    libelle = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)





class Users(models.Model):
    usergroup_id = models.IntegerField(blank=True, null=True)
    agent_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(blank=True, null=True)
    username = models.CharField(blank=True, null=True)
    password = models.CharField(blank=True, null=True)
    telephone = models.CharField(blank=True, null=True)
    email = models.CharField(blank=True, null=True)
    adresse = models.CharField(blank=True, null=True)
    statut = models.IntegerField(blank=True, null=True)
    isconnected = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)



class Ventefrs(models.Model):
    vente_id = models.IntegerField(blank=True, null=True)
    fournisseur_id = models.IntegerField(blank=True, null=True)
    chef_file = models.IntegerField(blank=True, null=True)
    offre_id = models.IntegerField(blank=True, null=True)
    asf = models.IntegerField(blank=True, null=True)
    asc = models.IntegerField(blank=True, null=True)
    ajt = models.IntegerField(blank=True, null=True)
    drtss = models.IntegerField(blank=True, null=True)
    rccm = models.IntegerField(blank=True, null=True)
    cnf = models.IntegerField(blank=True, null=True)
    caut = models.IntegerField(blank=True, null=True)



class Ventes(models.Model):
    num_vente = models.CharField(blank=True, null=True)
    lot_id = models.IntegerField(blank=True, null=True)
    fournisseur_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    date_vente = models.CharField(blank=True, null=True)
    heure_vente = models.CharField(blank=True, null=True)
    montant = models.CharField(blank=True, null=True)
    acheteur = models.CharField(blank=True, null=True)
    contact_acheteur = models.CharField(blank=True, null=True)
    statut = models.CharField(blank=True, null=True)
    grpent = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    observation = models.CharField(blank=True, null=True)





