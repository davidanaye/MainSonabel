from django import forms
from suivi.models import *



class PlanitemsForm(forms.ModelForm):
    class Meta:
        model = Planitems
        fields = '__all__'
        
        
        

class PlansForm(forms.ModelForm):
    class Meta:
        model = Plans
        fields = '__all__'
        
        
        
class DossierForm(forms.ModelForm):
    class Meta:
        model = Dossiers
        fields = '__all__'
        exclude = ('planitem_id', 'owner')
        widgets = {
            'date_trans_dgcmef': forms.DateInput(attrs={'type': 'date'}),
            'date_retour_dgcmef': forms.DateInput(attrs={'type': 'date'}),
            'date_trans_sign': forms.DateInput(attrs={'type': 'date'}),
            'date_retour_sign': forms.DateInput(attrs={'type': 'date'}),
            'intitule_doss': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
        }
        
        
        
        
class LotForm(forms.ModelForm):
    class Meta:
        model = Lots
        fields = '__all__'
        exclude = ('dossier_id',)
        widgets = {
            'intitule_lot': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
        }

    
        
class AvisForm(forms.ModelForm):
    class Meta:
        model = Avis
        exclude = ('dossier_id', 'date_envoi',)
        widgets = {
            'date_publi': forms.DateInput(attrs={'type': 'date'}),
            'date_lancement_pulication': forms.DateInput(attrs={'type': 'date'}),
        }
        labels = {
            'date_lancement_pulication': 'Date de lancement de la publication',
            'date_publi': 'Date de publication DGCMEF',
            'num_publi': 'Numéro de publication',
            'fichier': 'Avis de publication',
        }
        
class OffreForm(forms.ModelForm):
    entreprise = forms.ModelChoiceField(
        queryset=Fournisseurs.objects.all(),
        widget=forms.Select(attrs={
            'class': 'form-control select2',
            'placeholder': 'Sélectionnez ou ajoutez une entreprise',
        }),
        label="Entreprise",
        required=True
    )
    lot = forms.ModelChoiceField(
        queryset=Lots.objects.none(),
        widget=forms.RadioSelect,
        required=False,
        label="Lot"
    )

    class Meta:
        model = Offres
        fields = ['date_prevu_reception', 'entreprise', 'offre_technique', 'lot']

    def __init__(self, *args, **kwargs):
        dossier = kwargs.pop('dossier', None)
        super().__init__(*args, **kwargs)

        if dossier is not None:
            self.fields['lot'].queryset = Lots.objects.filter(dossier_id=dossier)

        # Actualisez la queryset pour inclure toutes les entreprises, y compris les nouvelles
        self.fields['entreprise'].queryset = Fournisseurs.objects.all()

    def clean_entreprise(self):
        entreprise = self.cleaned_data.get('entreprise')
        if entreprise:
            return entreprise
        else:
            entreprise_nom = self.data.get('entreprise')  # Nom de l'entreprise saisi
            if entreprise_nom:
                entreprise, created = Fournisseurs.objects.get_or_create(nom_four=entreprise_nom)
                return entreprise
            else:
                raise forms.ValidationError("Veuillez sélectionner ou ajouter une entreprise.")
class MarcheForm(forms.ModelForm):
    class Meta:
        model = Marches
        fields = ['offre', 'num_ref', 'date_notif', 'date_retour_sign', 'montant']
        labels = {
            'offre': 'Offre',
            'num_ref': 'Numéro de marché',
            'date_notif': 'Date de notification du projet de contrat',
            'date_retour_sign': 'Date de signature du contrat',
            'montant': 'Montant',
        }
        widgets = {
            'offre': forms.Select(attrs={'class': 'form-control', 'id': 'id_offre'}),
            'num_ref': forms.TextInput(attrs={'class': 'form-control'}),
            'date_notif': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'date_retour_sign': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'montant': forms.NumberInput(attrs={'step': 0.01, 'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Précharger les offres disponibles
        self.fields['offre'].queryset = Offres.objects.all()

        
class ResultatsForm(forms.ModelForm):
    class Meta:
        model = Resultats
        fields = ['date_prevu_pub', 'attributaire', 'observation', 'litige', 'fichier_litige', 'statut']
        labels = {
            'date_prevu_pub': 'Date de publication du résultat',
            'attributaire': 'Attributaire provisoire',
            'observation': 'Observation',
            'litige': 'Litige',
            'fichier_litige': 'Fichier Litige',
            'statut': 'Statut',
        }
        widgets = {
            'date_prevu_pub': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'attributaire': forms.Select(attrs={'class': 'form-control'}),
            'observation': forms.Textarea(attrs={'class': 'form-control'}),
            'litige': forms.Select(choices=[('Oui', 'Oui'), ('Non', 'Non')], attrs={'class': 'form-control', 'id': 'id_litige'}),
            'fichier_litige': forms.ClearableFileInput(attrs={'class': 'form-control', 'id': 'id_fichier_litige'}),
            'statut': forms.Select(choices=[('Retenu', 'Retenu'), ('Non Retenu', 'Non Retenu')], attrs={'class': 'form-control'}),
        }

    # Override the __init__ method to customize the queryset
    def __init__(self, *args, **kwargs):
        super(ResultatsForm, self).__init__(*args, **kwargs)
        self.fields['attributaire'].queryset = Fournisseurs.objects.all()
        self.fields['attributaire'].label_from_instance = lambda obj: obj.nom_four