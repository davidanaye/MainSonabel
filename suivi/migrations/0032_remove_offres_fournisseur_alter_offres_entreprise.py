# Generated by Django 5.0.1 on 2024-07-31 16:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suivi', '0031_remove_offres_lot_id_remove_offres_lots_offres_lot'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='offres',
            name='fournisseur',
        ),
        migrations.AlterField(
            model_name='offres',
            name='entreprise',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='offres', to='suivi.fournisseurs'),
        ),
    ]