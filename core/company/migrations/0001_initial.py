# Generated by Django 3.2.7 on 2021-10-17 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('companyName', models.CharField(default='Nombre compañia', max_length=120, null=True, verbose_name='Nombre Compañia')),
                ('companyLogo', models.ImageField(blank=True, help_text='jpg, png 2MB Max.', null=True, upload_to='company', verbose_name='Logo')),
                ('companyNit', models.CharField(default='0000000000-0', max_length=20, verbose_name='NIT')),
                ('companyAddress', models.CharField(blank=True, default='Direccion', max_length=60, null=True, verbose_name='Dirección')),
                ('companyCity', models.CharField(blank=True, max_length=60, null=True, verbose_name='Ciudad')),
            ],
            options={
                'verbose_name': 'Company',
                'verbose_name_plural': 'Companies',
                'db_table': 'Company',
            },
        ),
    ]
