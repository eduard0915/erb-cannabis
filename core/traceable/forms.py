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
        fields = 'seed_type', 'crop_type', 'geo_zone', 'plant_size', 'leaves_size', 'flowers_size', 'taxonomic', 'weight_collection', 'date_collection', 'reception_date', 'accepted_material', 'received_amount'

        widgets = {
            'crop_type': Select(attrs={'class': 'form-control', 'required': True}),
            'seed_type': Select(attrs={'class': 'form-control', 'required': True}),
            'geo_zone': TextInput(attrs={'class': 'form-control', 'required': True}),
            'taxonomic': TextInput(attrs={'class': 'form-control', 'required': True}),
            'accepted_material': NumberInput(attrs={'class': 'form-control', 'required': True}),
            'received_amount ': NumberInput(attrs={'class': 'form-control', 'required': True}),
            'plant_size': NumberInput(attrs={'class': 'form-control', 'required': True}),
            'leaves_size': NumberInput(attrs={'class': 'form-control', 'required': True}),
            'flowers_size': NumberInput(attrs={'class': 'form-control', 'required': True}),
            'weight_collection': NumberInput(attrs={'class': 'form-control', 'required': True}),
            'reception_date': DateInput(format='%Y-%m-%d', attrs= {
                'id': 'reception_date',
                'class': 'form-control datepicker'
            }),
            'date_collection': DateInput(format='%Y-%m-%d', attrs= {
                'id': 'date_collection',
                'class': 'form-control datepicker'
            })
        }

        exclude = [
            'classification_date',
            'control_number',
            'batch_number',
            'extract_batch_number',
            'extraction_date',
            'conc_batch_number',
            'conc_date',
            'isolate_batch_number',
            'isolate_date'
        ]

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data
