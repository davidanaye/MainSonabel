# Generated by Django 5.0.1 on 2024-07-16 21:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suivi', '0011_resultats'),
    ]

    operations = [
        migrations.AddField(
            model_name='resultats',
            name='offre',
            field=models.OneToOneField(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='resultat', to='suivi.offres'),
            preserve_default=False,
        ),
    ]
