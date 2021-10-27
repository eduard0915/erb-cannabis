from datetime import datetime

from crum import get_current_user
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from djchoices import ChoiceItem, DjangoChoices

from core.models import BaseModel


class CropType(DjangoChoices):
    greenhouse = ChoiceItem('Invernadero', 'Invernadero')
    free_environment = ChoiceItem('Ambiente Libre', 'Ambiente Libre')
    organic = ChoiceItem('Organico', 'Organico')


class SeedType(DjangoChoices):
    creole = ChoiceItem('Criolla', 'Criolla')
    improved = ChoiceItem('Mejorada', 'Mejorada')
    baby = ChoiceItem('Baby', 'Baby')
    hybrid = ChoiceItem('Hibrida', 'Hibrida')


class Traceability(BaseModel):
    seed_type = models.CharField(max_length=30, verbose_name='Tipo de Semilla', choices=SeedType.choices)
    crop_type = models.CharField(max_length=30, verbose_name='Tipo de Cultivo', choices=CropType.choices)
    geo_zone = models.CharField(max_length=50, verbose_name='Zona Geografica')
    plant_size = models.SmallIntegerField(verbose_name='Tamaño de la planta (cm)')
    leaves_size = models.SmallIntegerField(verbose_name='Tamaño de las hojas (cm)')
    flowers_size = models.SmallIntegerField(verbose_name='Tamaño de las flores (cm)')
    taxonomic = models.CharField(max_length=100, verbose_name='Clasificación Taxonomica')
    date_collection = models.DateField(verbose_name='Fecha de Recolección')
    reception_date = models.DateField(verbose_name='Fecha de Ingreso')
    weight_collection = models.SmallIntegerField(verbose_name='Peso de Material Recolectado (Kg)')
    accepted_material = models.SmallIntegerField(verbose_name='Peso de Material Aceptado (Kg)')
    classification_date = models.DateField(verbose_name='Fecha de Clasificación')
    control_number = models.CharField(max_length=15, verbose_name='N° de Control')
    batch_number = models.CharField(max_length=15, verbose_name='N° de Lote de Material Vegetal')
    extract_batch_number = models.CharField(max_length=15, verbose_name='N° de Lote de Extracto')
    extraction_date = models.DateField (verbose_name='Fecha de Extracción')
    conc_batch_number = models.CharField(max_length=15, verbose_name='N° de Lote de Concentrado')
    conc_date = models.DateField (verbose_name='Fecha de Concentración')
    isolate_batch_number = models.CharField(max_length=15, verbose_name='N° de Lote de Aislado')
    isolate_date = models.DateField (verbose_name='Fecha de Aislamiento')

    def __str__(self):
        return self.control_number

    class Meta:
        db_table = 'Traceability'
        verbose_name = 'Traceability'
        verbose_name_plural = 'Traceabilitys'

    @receiver(post_save, sender='traceable.Traceability')
    def post_save_function(sender, instance, **kwargs):
        if instance.control_number:
            return None
        date = datetime.now().strftime('%y%m%d%H%M')
        instance.control_number = date
        instance.save()

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None, *args, **kwargs):
        user = get_current_user()
        if user is not None:
            if not self.pk:
                self.user_creation = user
            else:
                self.user_updated = user
        # self.description_ext = self.description_ext.capitalize()
        return super(Traceability, self).save(*args, **kwargs)

