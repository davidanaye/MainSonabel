from django.db import models
from django.contrib.auth.models import User



class Fournisseurs(models.Model):
    nom_four = models.CharField(max_length=200, blank=True, null=True)
    rccm = models.CharField(max_length=200, blank=True, null=True)
    ifu = models.CharField(max_length=200, blank=True, null=True)
    telephone1 = models.CharField(max_length=200, blank=True, null=True)
    telephone2 = models.CharField(max_length=200, blank=True, null=True)
    adresse = models.CharField(max_length=200, blank=True, null=True)
    email = models.CharField(max_length=200, blank=True, null=True)
    domaine = models.CharField(max_length=200, blank=True, null=True)
    type = models.CharField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    
class Status(models.Model):
    libelle = models.CharField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True,blank=True, null=True)
    updated_at = models.DateTimeField(auto_now_add=True,blank=True, null=True)
    
    def __str__(self):
        return self.libelle
    
    
    
class Modes(models.Model):
    libelle = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True,blank=True, null=True)
    updated_at = models.DateTimeField(auto_now_add=True,blank=True, null=True)
    
    def __str__(self):
        return self.libelle
    
    
    
class Devises(models.Model):
    libelle = models.CharField(max_length=200, blank=True, null=True)
    symbole = models.CharField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True,blank=True, null=True)
    updated_at = models.DateTimeField(auto_now_add=True,blank=True, null=True)
    
    def __str__(self):
        return self.libelle
    
    

class Budgets(models.Model):
    libelle = models.CharField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True,blank=True, null=True)
    updated_at = models.DateTimeField(auto_now_add=True,blank=True, null=True)
    
    def __str__(self):
        return self.libelle


class Plans(models.Model):
    annee = models.IntegerField(blank=True, null=True)
    date_plan = models.DateField(blank=True, null=True)
    statut = models.ForeignKey(Status, blank=True, null=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True,blank=True, null=True)
    updated_at = models.DateTimeField(auto_now_add=True,blank=True, null=True)

    
    def __str__(self):
        return str(self.annee)


class Planitems(models.Model):
    num_ordre =  models.CharField(max_length=200, blank=True, null=True)
    plan_id = models.ForeignKey(Plans, blank=True, null=True, on_delete=models.CASCADE, verbose_name="PPM")
    budget = models.CharField(max_length=200,blank=True, null=True)
    typcredit = models.CharField(max_length=200,blank=True, null=True)
    immobilisation = models.CharField(max_length=200,blank=True, null=True)
    credit = models.CharField(max_length=200,blank=True, null=True)
    centre_cout = models.CharField(max_length=200,blank=True, null=True)
    projet = models.CharField(max_length=200,blank=True, null=True)
    localisation = models.CharField(max_length=200,blank=True, null=True)
    montant_estime = models.CharField(max_length=200, blank=True, null=True)
    composante = models.CharField(max_length=200,blank=True, null=True)
    montant_dispo =  models.CharField(max_length=200, blank=True, null=True)
    designation = models.CharField(max_length=200,blank=True, null=True)
    type = models.CharField(max_length=200,blank=True, null=True)
    mode = models.CharField(max_length=200,blank=True, null=True)
    nbr_lot = models.CharField(max_length=200,blank=True, null=True)
    agent_id = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE, verbose_name="Agent en charge")
    date_tech = models.CharField(max_length=200,blank=True, null=True)
    date_tech_reel = models.CharField(max_length=200,blank=True, null=True)
    date_dgcmef = models.CharField(max_length=200,blank=True, null=True)
    date_dgcmef_reel = models.CharField(max_length=200,blank=True, null=True)
    date_off = models.CharField(max_length=200,blank=True, null=True)
    date_off_reel = models.CharField(max_length=200,blank=True, null=True)
    temp = models.IntegerField(blank=True, null=True)
    temp_reel = models.IntegerField(blank=True, null=True)
    date_resultat = models.CharField(max_length=200,blank=True, null=True)
    resultat = models.CharField(max_length=200,blank=True, null=True)
    date_visite_site = models.CharField(max_length=200,blank=True, null=True)
    date_demarrage = models.CharField(max_length=200,blank=True, null=True)
    date_reel_demarrage = models.CharField(max_length=200,blank=True, null=True)
    delai_exe = models.IntegerField(blank=True, null=True)
    delai_reel_exe = models.IntegerField(blank=True, null=True)
    date_butoir = models.CharField(max_length=200,blank=True, null=True)
    date_reel_fin = models.CharField(max_length=200,blank=True, null=True)
    budget_travaux = models.CharField(max_length=200,blank=True, null=True)
    observation = models.CharField(max_length=200,blank=True, null=True)
    statut = models.CharField(max_length=200,blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return str(self.num_ordre)



class Dossiers(models.Model):
    planitem_id = models.ForeignKey(Planitems, blank=True, null=True, on_delete=models.CASCADE, verbose_name="Ligne du plan")
    numero_doss = models.CharField(max_length=200,blank=True, null=True)
    intitule_doss = models.TextField(blank=True, null=True)
    date_trans_sign = models.DateField(blank=True, null=True, verbose_name="Date envois pour signature")
    date_retour_sign = models.DateField(blank=True, null=True, verbose_name="Date retour")
    date_trans_dgcmef = models.DateField(blank=True, null=True, verbose_name="Date de tensmission à la DGCMEF")
    owner = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE, verbose_name="Propriétaire")
    date_retour_dgcmef = models.DateField(blank=True, null=True, verbose_name="Date retour la DGCMEF")
    fichier = models.FileField(blank=True, null=True, upload_to="uploads/dao")
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    
    
    
    def __str__(self):
        return self.numero_doss + ' - ' + self.intitule_doss  
    
    
    def has_lots(self):
        # Check if this dossier have a lot
        return self.lots_set.exists()
    
    
    
class Lots(models.Model):
    dossier_id = models.ForeignKey(Dossiers, on_delete=models.CASCADE, blank=True, null=True, verbose_name="Dossier")
    num_lot = models.CharField(max_length=200, blank=True, null=True,  verbose_name="Numero du lot")
    intitule_lot = models.TextField(blank=True, null=True,  verbose_name="Intitulé du lot")
    montant_lot = models.IntegerField(blank=True, null=True,  verbose_name="Montant du lot")
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    
    
    def __str__(self):
        return self.intitule_lot
    

    
class Avis(models.Model):
    num_publi = models.CharField(max_length=200, blank=True, null=True, verbose_name="Numero de publication")
    date_envoi = models.DateField(blank=True, null=True, verbose_name="Date d'envois")
    date_publi = models.DateTimeField(blank=True, null=True, verbose_name="Date de publication")
    fichier = models.FileField(upload_to="uploads/avis", blank=True, null=True, verbose_name="Avis de publication")
    dossier_id = models.ForeignKey(Dossiers, blank=True, null=True, verbose_name="Dossier", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    

class Offres(models.Model):
    dossier = models.ForeignKey(Dossiers, on_delete=models.CASCADE, verbose_name="Dossier")
    updated_at = models.DateTimeField(blank=True, null=True)
    off_doss_id = models.IntegerField(blank=True, null=True)
    lot_id = models.IntegerField(blank=True, null=True)
    entreprise_cons = models.IntegerField(blank=True, null=True)
    date_depot = models.CharField(max_length=100, blank=True, null=True)
    heure_depot = models.CharField(max_length=100, blank=True, null=True)
    nom_prenom_dep = models.CharField(max_length=100, blank=True, null=True)
    telephone_dep = models.CharField(max_length=15, blank=True, null=True)
    montant = models.IntegerField(blank=True, null=True)
    montant_corr = models.IntegerField(blank=True, null=True)
    devise = models.CharField(max_length=10, blank=True, null=True)
    taxe = models.CharField(max_length=10, blank=True, null=True)
    montant2 = models.IntegerField(blank=True, null=True)
    montant2_corr = models.IntegerField(blank=True, null=True)
    devise2 = models.CharField(max_length=10, blank=True, null=True)
    taxe2 = models.CharField(max_length=10, blank=True, null=True)
    montant3 = models.IntegerField(blank=True, null=True)
    montant3_corr = models.IntegerField(blank=True, null=True)
    devise3 = models.CharField(max_length=10, blank=True, null=True)
    taxe3 = models.CharField(max_length=10, blank=True, null=True)
    montant4 = models.IntegerField(blank=True, null=True)
    montant4_corr = models.IntegerField(blank=True, null=True)
    devise4 = models.CharField(max_length=10, blank=True, null=True)
    taxe4 = models.CharField(max_length=10, blank=True, null=True)
    montant_offre = models.IntegerField(blank=True, null=True)
    montant_corrige = models.IntegerField(blank=True, null=True)
    devise_offre = models.CharField(max_length=10, blank=True, null=True)
    taxe_offre = models.CharField(max_length=10, blank=True, null=True)
    aucun_pli = models.IntegerField(blank=True, null=True)
    asf = models.IntegerField(blank=True, null=True)
    asc = models.IntegerField(blank=True, null=True)
    ajt = models.IntegerField(blank=True, null=True)
    drtss = models.IntegerField(blank=True, null=True)
    rccm = models.IntegerField(blank=True, null=True)
    cnf = models.IntegerField(blank=True, null=True)
    caut = models.IntegerField(blank=True, null=True)
    fichier_caution = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
   

class Marches(models.Model):
    mar_doss_id = models.IntegerField(blank=True, null=True)
    lot_id = models.IntegerField(blank=True, null=True)
    num_ref = models.CharField(max_length=100, blank=True, null=True)
    objet = models.CharField(max_length=255, blank=True, null=True)
    date_appro = models.CharField(max_length=100, blank=True, null=True)
    date_notif = models.CharField(max_length=100, blank=True, null=True)
    montant = models.IntegerField(blank=True, null=True)
    devise = models.CharField(max_length=10, blank=True, null=True)
    taxe = models.CharField(max_length=10, blank=True, null=True)
    montant2 = models.IntegerField(blank=True, null=True)
    devise2 = models.CharField(max_length=10, blank=True, null=True)
    taxe2 = models.CharField(max_length=10, blank=True, null=True)
    montant3 = models.IntegerField(blank=True, null=True)
    devise3 = models.CharField(max_length=10, blank=True, null=True)
    taxe3 = models.CharField(max_length=10, blank=True, null=True)
    montant4 = models.IntegerField(blank=True, null=True)
    devise4 = models.CharField(max_length=10, blank=True, null=True)
    taxe4 = models.CharField(max_length=10, blank=True, null=True)
    montant_total = models.IntegerField(blank=True, null=True)
    devise_total = models.CharField(max_length=10, blank=True, null=True)
    taxe_total = models.CharField(max_length=10, blank=True, null=True)
    delai = models.CharField(max_length=100, blank=True, null=True)
    attributaire = models.IntegerField(blank=True, null=True)
    date_rem_sign = models.CharField(max_length=100, blank=True, null=True)
    date_retour_sign = models.CharField(max_length=100, blank=True, null=True)
    date_rem_enr = models.CharField(max_length=100, blank=True, null=True)
    date_retour_enr = models.CharField(max_length=100, blank=True, null=True)
    marche = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    dossier_id = models.ForeignKey(Dossiers, blank=True, null=True, verbose_name="Dossier", on_delete=models.CASCADE)