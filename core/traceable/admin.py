from django.contrib import admin
from core.traceable.models import Traceability


class TraceabilityAdmin(admin.ModelAdmin):
    list_display = ('seed_type', 'crop_type', 'geo_zone', 'plant_size', 'leaves_size', 'flowers_size')

admin.site.register(Traceability, TraceabilityAdmin)
