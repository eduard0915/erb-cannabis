# Generated by Django 3.2.8 on 2021-10-29 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('traceable', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='traceability',
            name='accepted_material',
            field=models.SmallIntegerField(blank=True, null=True, verbose_name='Peso de Material Aceptado (Kg)'),
        ),
    ]