from django.db import models
from django.contrib.auth.models import User


class Budgets(models.Model):
    nom = models.CharField(max_length=100)
  
class Status(models.Model):
    nom = models.CharField(max_length=100)

class Modes(models.Model):
    nom = models.CharField(max_length=100)    

class Devises(models.Model):
    nom = models.CharField(max_length=100)    
    
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
    
    def __str__(self):
        return self.nom_four
    

class Plans(models.Model):
    annee = models.IntegerField(blank=True, null=True)
    date_plan = models.DateField(blank=True, null=True)
    statut = models.ForeignKey('Status', blank=True, null=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True,blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return f"{self.annee}"

class Planitems(models.Model):
    agent_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    annee = models.ForeignKey('Plans', on_delete=models.CASCADE, null=True, blank=True)
    num_ordre = models.TextField(null=True, blank=True)
    num_credit = models.TextField(null=True, blank=True)
    budget = models.TextField(null=True, blank=True)
    direction_charge_dossier = models.TextField(null=True, blank=True)
    unite_service_beneficiaire = models.TextField(null=True, blank=True)
    montant_inscription_budgetaire = models.TextField(null=True, blank=True)
    montant_depenses_engagees_non_liquidees = models.TextField(null=True, blank=True)
    disponible = models.TextField(null=True, blank=True)
    elements_composantes = models.TextField(null=True, blank=True)
    type_prestation = models.TextField(null=True, blank=True)
    nature_prestations = models.TextField(null=True, blank=True)
    mode_passation = models.TextField(null=True, blank=True)
    agent_charge_dossier = models.TextField(null=True, blank=True)
    date_prevue_reception_dossier_technique = models.TextField(null=True, blank=True)
    date_reelle_reception_dossier_technique = models.TextField(null=True, blank=True)
    service_charge_dossier_technique = models.TextField(null=True, blank=True)
    intitule_dossier = models.TextField(null=True, blank=True)
    ref_dossier_appel_concurrence = models.TextField(null=True, blank=True)
    dossiers_non_recus_montant_alloue = models.TextField(null=True, blank=True)
    taux_reception_dossiers_dmp = models.TextField(null=True, blank=True)
    nombre_dossiers_recus = models.TextField(null=True, blank=True)
    date_transmission_signature = models.TextField(null=True, blank=True)
    date_retour_signature = models.TextField(null=True, blank=True)
    date_transmission_par_dgcmef = models.TextField(null=True, blank=True)
    date_prevue_lancement_dgcmef = models.TextField(null=True, blank=True)
    date_reelle_lancement_dgcmef = models.TextField(null=True, blank=True)
    dossiers_non_lances_montant_alloue = models.TextField(null=True, blank=True)
    taux_lancement_dossiers = models.TextField(null=True, blank=True)
    nombre_dossiers_lances = models.TextField(null=True, blank=True)
    date_prevue_remise_offres = models.TextField(null=True, blank=True)
    date_reelle_remise_offres = models.TextField(null=True, blank=True)
    convocation_ouverture = models.TextField(null=True, blank=True)
    transmission_pv_signature = models.TextField(null=True, blank=True)
    retour_signature_pv = models.TextField(null=True, blank=True)
    transmission_dgcmef_eventuel = models.TextField(null=True, blank=True)
    temps_necessaire_evaluation_offres_jours = models.TextField(null=True, blank=True)
    convocation_analyses_offres = models.TextField(null=True, blank=True)
    date_effectives_analyses_offres = models.TextField(null=True, blank=True)
    duree_reelle_evaluation_offres_jours = models.TextField(null=True, blank=True)
    date_introduction_signature = models.TextField(null=True, blank=True)
    date_retour_signature_dg = models.TextField(null=True, blank=True)
    date_transmission_dgcmef = models.TextField(null=True, blank=True)
    observations_eventuelles_dgcmef = models.TextField(null=True, blank=True)
    reference_publication = models.TextField(null=True, blank=True)
    publication_dgcmef = models.TextField(null=True, blank=True)
    nom_attributaire_provisoire = models.TextField(null=True, blank=True)
    contentieux_litiges = models.TextField(null=True, blank=True)
    montant = models.TextField(null=True, blank=True)
    numero_marche = models.TextField(null=True, blank=True)
    date_notification_projet_contrat = models.TextField(null=True, blank=True)
    date_signature_contrat = models.TextField(null=True, blank=True)
    dossiers_marches_non_conclu_montant_alloue = models.TextField(null=True, blank=True)
    taux_passation_marches = models.TextField(null=True, blank=True)
    nombre_marches_conclure_par_ligne_ppm = models.TextField(null=True, blank=True)
    nombre_marches_conclus_par_ligne_ppm = models.TextField(null=True, blank=True)
    nombre_ligne_fait_objet_marche = models.TextField(null=True, blank=True)
    date_remise_garantie_bonne_execution = models.TextField(null=True, blank=True)
    date_transmission_contrat_enregistrement = models.TextField(null=True, blank=True)
    date_retour_enregistrement_contrat = models.TextField(null=True, blank=True)
    date_emission_ordre_service = models.TextField(null=True, blank=True)
    date_remise_site = models.TextField(null=True, blank=True)
    date_demarrage_prevue_execution = models.TextField(null=True, blank=True)
    date_reelle_demarrage_execution = models.TextField(null=True, blank=True)
    delai_prevue_execution = models.TextField(null=True, blank=True)
    delai_reelle_execution = models.TextField(null=True, blank=True)
    date_butoir = models.TextField(null=True, blank=True)
    gestionnaire_credit = models.TextField(null=True, blank=True)
    date_reelle_lancement = models.TextField(null=True, blank=True)
    execution_ppm_2023_30_septembre = models.TextField(null=True, blank=True)
    observations_suivi_quotidien_04_12_2023 = models.TextField(null=True, blank=True)
    dossiers_recus = models.TextField(null=True, blank=True)
    dossiers_lances_non_encore_attribues = models.TextField(null=True, blank=True)
    marches_en_cours_execution = models.TextField(null=True, blank=True)
    marches_executes = models.TextField(null=True, blank=True)
    types = models.TextField(null=True, blank=True)
    observations = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return f"{self.annee} - {self.num_ordre}"



class Dossiers(models.Model):
    planitem_id = models.ForeignKey('Planitems', blank=True, null=True, on_delete=models.CASCADE, verbose_name="Ligne du plan")
    numero_doss = models.CharField(max_length=200, blank=True, null=True)
    intitule_doss = models.TextField(blank=True, null=True)
    date_trans_sign = models.DateField(blank=True, null=True, verbose_name="Date envois pour signature")
    date_retour_sign = models.DateField(blank=True, null=True, verbose_name="Date retour")
    date_trans_dgcmef = models.DateField(blank=True, null=True, verbose_name="Date de transmission à la DGCMEF")
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, verbose_name="Propriétaire")
    date_retour_dgcmef = models.DateField(blank=True, null=True, verbose_name="Date retour la DGCMEF")
    fichier = models.FileField(blank=True, null=True, upload_to="uploads/dao")
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.numero_doss + ' - ' + self.intitule_doss
    
    def has_lots(self):
        # Check if this dossier has lots
        return self.lots_set.exists()
    
    
    
class Lots(models.Model):
    dossier_id = models.ForeignKey(Dossiers, on_delete=models.CASCADE, blank=True, null=True, verbose_name="Dossier")
    num_lot = models.CharField(max_length=200, blank=True, null=True,  verbose_name="Numero du lot")
    intitule_lot = models.TextField(blank=True, null=True,  verbose_name="Intitulé du lot")
    montant_lot = models.IntegerField(blank=True, null=True,  verbose_name="Montant du lot")
    marche = models.ForeignKey('Marches', on_delete=models.SET_NULL, blank=True, null=True, related_name='lots', verbose_name="Marché")
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.intitule_lot

    

    
class Avis(models.Model):
    num_publi = models.CharField(max_length=200, blank=True, null=True, verbose_name="Numero de publication")
    date_envoi = models.DateField(blank=True, null=True, verbose_name="Date d'envois")
    date_publi = models.DateTimeField(blank=True, null=True, verbose_name="Date de publication DGCMEF")
    fichier = models.FileField(upload_to="uploads/avis", blank=True, null=True, verbose_name="Avis de publication")
    dossier_id = models.ForeignKey(Dossiers, blank=True, null=True, verbose_name="Dossier", on_delete=models.CASCADE)
    date_lancement_pulication = models.DateField(blank=True, null=True, verbose_name="Date de lancement de publication")
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    
class Offres(models.Model):
    dossier = models.ForeignKey(Dossiers, on_delete=models.CASCADE, verbose_name="Dossier")
    lot = models.ForeignKey(Lots, on_delete=models.SET_NULL, verbose_name="Lot", null=True, blank=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    off_doss_id = models.IntegerField(blank=True, null=True)  
    date_prevu_reception = models.DateField(blank=True, null=True, verbose_name="Date prévue de réception des offres")
    date_reel_reception = models.DateField(blank=True, null=True, verbose_name="Date réelle de réception des offres")
    entreprise = models.ForeignKey(Fournisseurs, on_delete=models.SET_NULL, null=True, blank=True, related_name='offres')
    offre_technique = models.FileField(upload_to='uploads/offres_techniques/', blank=True, null=True, verbose_name="Offre technique")

    def __str__(self):
        return f"Offre {self.id} pour {self.dossier}"



class Resultats(models.Model):
    dossier_id = models.IntegerField(blank=True, null=True)
    date_par_res = models.CharField(max_length=100, blank=True, null=True)
    num_par_res = models.CharField(max_length=100, blank=True, null=True)
    attributaire = models.ForeignKey(
        'Fournisseurs',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='resultats'
     )
    litige = models.CharField(max_length=3, choices=[('Oui', 'Oui'), ('Non', 'Non')],blank=True, null=True)
    fichierpub = models.CharField(max_length=255, blank=True, null=True)
    fichier_litige = models.FileField(upload_to='litiges/', blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    date_prevu_pub = models.DateField(blank=True, null=True)
    date_reelle_pub = models.DateField(blank=True, null=True)
    observation = models.TextField(blank=True, null=True)
    statut = models.CharField(max_length=10, choices=[('Retenu', 'Retenu'), ('Non Retenu', 'Non Retenu')], blank=True, null=True)
    offre = models.OneToOneField('Offres', on_delete=models.CASCADE, related_name='resultat')
    lot = models.ForeignKey('Lots', on_delete=models.CASCADE, related_name='resultats', null=True, blank=True)

    def __str__(self):
        return f"Résultat pour Offre {self.offre} - Lot {self.lot}"


class Marches(models.Model):
    id = models.AutoField(primary_key=True)
    offre = models.ForeignKey(Offres, blank=True, null=True, verbose_name="Offre", on_delete=models.CASCADE)
    dossier = models.ForeignKey(Dossiers, blank=True, null=True, verbose_name="Dossier", on_delete=models.CASCADE)
    resultat = models.ForeignKey(Resultats, blank=True, null=True, verbose_name="Résultat", on_delete=models.CASCADE)
    num_ref = models.CharField(max_length=100, blank=True, null=True)
    date_notif = models.DateField(blank=True, null=True)  # Changez en DateField
    montant = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)  # Changez en DecimalField
    attributaire = models.ForeignKey(
        'Fournisseurs',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='marches'
    )
    date_retour_sign = models.DateField(blank=True, null=True)  # Changez en DateField
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return f"Marché {self.num_ref} - Dossier {self.dossier} - Offre {self.offre}"