# Generated by Django 3.2.7 on 2021-09-22 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_user_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='user/%Y%m%d', verbose_name='Foto'),
        ),
    ]
