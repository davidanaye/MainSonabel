# Generated by Django 5.0.1 on 2024-08-07 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suivi', '0032_remove_offres_fournisseur_alter_offres_entreprise'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='offres',
            name='ajt',
        ),
        migrations.RemoveField(
            model_name='offres',
            name='asc',
        ),
        migrations.RemoveField(
            model_name='offres',
            name='asf',
        ),
        migrations.RemoveField(
            model_name='offres',
            name='aucun_pli',
        ),
        migrations.RemoveField(
            model_name='offres',
            name='caut',
        ),
        migrations.RemoveField(
            model_name='offres',
            name='cnf',
        ),
        migrations.RemoveField(
            model_name='offres',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='offres',
            name='date_depot',
        ),
        migrations.RemoveField(
            model_name='offres',
            name='devise',
        ),
        migrations.RemoveField(
            model_name='offres',
            name='devise2',
        ),
        migrations.RemoveField(
            model_name='offres',
            name='devise3',
        ),
        migrations.RemoveField(
            model_name='offres',
            name='devise4',
        ),
        migrations.RemoveField(
            model_name='offres',
            name='devise_offre',
        ),
        migrations.RemoveField(
            model_name='offres',
            name='drtss',
        ),
        migrations.RemoveField(
            model_name='offres',
            name='entreprise_cons',
        ),
        migrations.RemoveField(
            model_name='offres',
            name='fichier_caution',
        ),
        migrations.RemoveField(
            model_name='offres',
            name='heure_depot',
        ),
        migrations.RemoveField(
            model_name='offres',
            name='montant',
        ),
        migrations.RemoveField(
            model_name='offres',
            name='montant2',
        ),
        migrations.RemoveField(
            model_name='offres',
            name='montant2_corr',
        ),
        migrations.RemoveField(
            model_name='offres',
            name='montant3',
        ),
        migrations.RemoveField(
            model_name='offres',
            name='montant3_corr',
        ),
        migrations.RemoveField(
            model_name='offres',
            name='montant4',
        ),
        migrations.RemoveField(
            model_name='offres',
            name='montant4_corr',
        ),
        migrations.RemoveField(
            model_name='offres',
            name='montant_corr',
        ),
        migrations.RemoveField(
            model_name='offres',
            name='montant_corrige',
        ),
        migrations.RemoveField(
            model_name='offres',
            name='montant_offre',
        ),
        migrations.RemoveField(
            model_name='offres',
            name='nom_prenom_dep',
        ),
        migrations.RemoveField(
            model_name='offres',
            name='rccm',
        ),
        migrations.RemoveField(
            model_name='offres',
            name='taxe',
        ),
        migrations.RemoveField(
            model_name='offres',
            name='taxe2',
        ),
        migrations.RemoveField(
            model_name='offres',
            name='taxe3',
        ),
        migrations.RemoveField(
            model_name='offres',
            name='taxe4',
        ),
        migrations.RemoveField(
            model_name='offres',
            name='taxe_offre',
        ),
        migrations.RemoveField(
            model_name='offres',
            name='telephone_dep',
        ),
        migrations.AlterField(
            model_name='marches',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='marches',
            name='date_notif',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='marches',
            name='date_retour_sign',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='marches',
            name='montant',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='marches',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
