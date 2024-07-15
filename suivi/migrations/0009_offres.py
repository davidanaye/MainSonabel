# Generated by Django 5.0.1 on 2024-07-01 13:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suivi', '0008_alter_avis_created_at_alter_avis_updated_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Offres',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('off_doss_id', models.IntegerField(blank=True, null=True)),
                ('lot_id', models.IntegerField(blank=True, null=True)),
                ('entreprise_cons', models.IntegerField(blank=True, null=True)),
                ('date_depot', models.CharField(blank=True, max_length=100, null=True)),
                ('heure_depot', models.CharField(blank=True, max_length=100, null=True)),
                ('nom_prenom_dep', models.CharField(blank=True, max_length=100, null=True)),
                ('telephone_dep', models.CharField(blank=True, max_length=15, null=True)),
                ('montant', models.IntegerField(blank=True, null=True)),
                ('montant_corr', models.IntegerField(blank=True, null=True)),
                ('devise', models.CharField(blank=True, max_length=10, null=True)),
                ('taxe', models.CharField(blank=True, max_length=10, null=True)),
                ('montant2', models.IntegerField(blank=True, null=True)),
                ('montant2_corr', models.IntegerField(blank=True, null=True)),
                ('devise2', models.CharField(blank=True, max_length=10, null=True)),
                ('taxe2', models.CharField(blank=True, max_length=10, null=True)),
                ('montant3', models.IntegerField(blank=True, null=True)),
                ('montant3_corr', models.IntegerField(blank=True, null=True)),
                ('devise3', models.CharField(blank=True, max_length=10, null=True)),
                ('taxe3', models.CharField(blank=True, max_length=10, null=True)),
                ('montant4', models.IntegerField(blank=True, null=True)),
                ('montant4_corr', models.IntegerField(blank=True, null=True)),
                ('devise4', models.CharField(blank=True, max_length=10, null=True)),
                ('taxe4', models.CharField(blank=True, max_length=10, null=True)),
                ('montant_offre', models.IntegerField(blank=True, null=True)),
                ('montant_corrige', models.IntegerField(blank=True, null=True)),
                ('devise_offre', models.CharField(blank=True, max_length=10, null=True)),
                ('taxe_offre', models.CharField(blank=True, max_length=10, null=True)),
                ('aucun_pli', models.IntegerField(blank=True, null=True)),
                ('asf', models.IntegerField(blank=True, null=True)),
                ('asc', models.IntegerField(blank=True, null=True)),
                ('ajt', models.IntegerField(blank=True, null=True)),
                ('drtss', models.IntegerField(blank=True, null=True)),
                ('rccm', models.IntegerField(blank=True, null=True)),
                ('cnf', models.IntegerField(blank=True, null=True)),
                ('caut', models.IntegerField(blank=True, null=True)),
                ('fichier_caution', models.CharField(blank=True, max_length=100, null=True)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('dossier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='suivi.dossiers', verbose_name='Dossier')),
            ],
        ),
    ]
