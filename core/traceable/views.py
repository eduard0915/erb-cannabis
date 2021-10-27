from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView, ListView

from core.traceable.forms import VegetalMaterialForms
from core.traceable.models import Traceability


class VegetalMaterialCreate(CreateView):
    model = Traceability
    form_class = VegetalMaterialForms
    template_name = 'create_material.html'
    # success_url =
    # url_redirect = success_url

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        global form
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                form = self.get_form()
                if form.is_valid():
                    form.save()
                    messages.success(request, f'Registro de material vegetal realizado satisfactoriamente!')
                else:
                    messages.error(request, form.errors)
            else:
                data['error'] = 'No ha ingresado datos en los campos'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Registro de Material Vegetal'
        context['list_url'] = reverse_lazy('traceable:material_list')
        context['action'] = 'add'
        context['entity'] = 'Registro de Material Vegetal'
        return context

# Listado de usuarios
class VegetalMaterialListView(LoginRequiredMixin, ListView):
    model = Traceability
    template_name = 'list_material.html'
    # permission_required = 'user.view_user'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                material = list(Traceability.objects.values(
                    'id',
                    'seed_type',
                    'crop_type',
                    'geo_zone',
                    'plant_size',
                    'leaves_size',
                    'flowers_size',
                    'taxonomic',
                    'weight_collection',
                    'date_collection',
                    'reception_date'
                ).order_by('-id'))
                return JsonResponse(material, safe=False)
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Lotes Cannabis'
        context['create_url'] = reverse_lazy('traceable:material_create')
        context['entity'] = 'Lotes Cannabis'
        return context