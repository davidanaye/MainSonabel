# Generated by Django 5.0.1 on 2024-07-23 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suivi', '0018_remove_marches_date_appro_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='offres',
            name='lots',
            field=models.ManyToManyField(blank=True, to='suivi.lots', verbose_name='Lots'),
        ),
    ]