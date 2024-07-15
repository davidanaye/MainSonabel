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
        fields = '__all__'
        exclude = ('dossier_id',)
        widgets = {
            'date_envoi': forms.DateInput(attrs={'type': 'date'}),
            'date_publi': forms.DateInput(attrs={'type': 'date'}),
        }
        
class OffreForm(forms.ModelForm):
    class Meta:
        model = Offres
        exclude = ('updated_at',)
        # widgets = {
        #     'om_prenom_dep': forms.DateInput(attrs={'type': 'date'}),
        #     'taxe_offre': forms.DateInput(attrs={'type': 'date'}),
        #     'rccm': forms.DateInput(attrs={'type': 'date'}),
        #     'fichier_caution': forms.DateInput(attrs={'type': 'date'}),
        #     'entreprise_cons': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
        # }
            


class MarcheForm(forms.ModelForm):
    class Meta:
        model = Marches
        fields = '__all__'
        
      