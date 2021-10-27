from django.forms import *
from core.traceable.models import Traceability


class VegetalMaterialForms(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['autocomplete'] = 'off'
            form.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Traceability
        fields = ('seed_type',
                  'crop_type',
                  'geo_zone',
                  'plant_size',
                  'leaves_size',
                  'flowers_size',
                  'taxonomic',
                  'weight_collection',
                  'date_collection',
                  'reception_date'
                  )
        widgets = {
            'crop_type': Select(attrs={'class': 'form-control', 'required': True}),
            'seed_type': Select(attrs={'class': 'form-control', 'required': True}),
            'geo_zone': TextInput(attrs={'class': 'form-control', 'required': True}),
        }

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                data = form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data
