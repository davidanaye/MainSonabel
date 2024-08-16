# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('LignePlan/', views.itemsliste, name='itemsliste'),  
    path('LignePlan/Ajout/', views.addplanitems, name='addplanitems'),
    path('LignePlan/Edit/<int:id>/', views.editplanitems, name='editplanitems'),
    path('LignePlan/Delete/<int:id>/', views.delete_planitem, name='delete_planitem'),
    path('LignePlan/Dossier', views.dossier, name='dossier'),
    path('LignePlan/Dossier/Liste', views.listdoc, name='listdoc'),
    path('LignePlan/AddDossier/<int:id>/', views.adddossier, name='adddossier'),
    path('LignePlan/EditDossier/<int:dossier_id>/', views.editdossier, name='editdossier'),
    path('LignePlan/Dossier/Delete/<int:dossier_id>/', views.delete_dossier, name='delete_dossier'),
    path('LignePlan/Dossier/Addlot/<int:id>/', views.adddlot, name='adddlot'),
    path('LignePlan/EditLot/<int:id>/', views.editlot, name='editlot'),
    path('LignePlan/DeleteLot/<int:lot_id>/', views.delete_lot, name='delete_lot'),
    path('LignePlan/Dossier/<int:dossier_id>/lots/', views.list_dossier_lots, name='dossier_lots'),
    path('LignePlan/Dossier/Suivi/', views.suivi, name='suivi'),
    path('LignePlan/Dossier/Traitement/<int:dossier_id>/', views.process_dossier, name='process_dossier'),
    path('LignePlan/Dossier/Traitement/Offre/<int:dossier_id>/', views.addoffre, name='addoffre'),
    path('LignePlan/Dossier/Traitement/Avis/Edit/<int:avis_id>/', views.editavis, name='editavis'),
    path('LignePlan/Dossier/Traitement/resultat/<int:offre_id>/', views.addresultat, name='addresultat'),
    path('LignePlan/Dossier/Traitement/Marche/<int:dossier_id>/', views.addmarche, name='addmarche'),
    
    path('LignePlan/Dossier/Traitement/editOffre/<int:dossier_id>/<int:offre_id>/', views.modifier_offres, name='modifier_offres'), 
    path('LignePlan/Dossier/Traitement/supprimerOffre/<int:dossier_id>/<int:offre_id>/', views.supprimer_offres, name='supprimer_offres'),
    path('LignePlan/Dossier/Traitement/editResultat/<int:dossier_id>/<int:resultat_id>/', views.modifier_resultat, name='modifier_resultat'), 
    path('LignePlan/Dossier/Traitement/supprimerResultat/<int:dossier_id>/<int:resultat_id>/', views.supprimer_resultat, name='supprimer_resultat'),
      path('LignePlan/Dossier/Traitement/editMarche/<int:dossier_id>/<int:marche_id>/', views.modifier_marche, name='modifier_marche'),
    path('LignePlan/Dossier/Traitement/supprimerMarche/<int:dossier_id>/<int:marche_id>/', views.supprimer_marche, name='supprimer_marche'),
    path('etat/', views.etat_dossiers, name='etat_dossiers'),
     path('LignePlan/Dossier/Traitement/Avis/<int:dossier_id>/', views.addavis, name='addavis'),
     path('avis/<int:avis_id>/delete/', views.deleteavis, name='deleteavis'), 
     path('add_new_entreprise/', views.add_new_entreprise, name='add_new_entreprise'),
     path('get_attributaire/', views.get_attributaire, name='get_attributaire'),
      path('LignePlan/import/', views.import_plan, name='import_plan'),
     path('filter_plan/', views.filter_plan, name='filter_plan'),
     path('ppm/<int:plan_id>/', views.ppm_view, name='ppm_view'),
     

]
