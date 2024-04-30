from django.shortcuts import render, redirect, get_object_or_404
from django.db import transaction
from django.views.decorators.csrf import csrf_protect
from django.db.models import Max, Count
from django.http import HttpResponse, HttpResponseBadRequest
from .models import Car
from .forms import CarForm
from django.http import JsonResponse
import json
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.
class car_list(ListView):
    model = Car
    template_name = 'car_app/car_list.html'
    queryset = Car.objects.order_by("position")
    context_object_name = 'cars'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['car_colors'] = Car.objects.values('color').annotate(count=Count('id'))
        return context
class show_car(ListView):
    model = Car
    template_name = 'car_app/show_car.html'
    context_object_name = 'cars'
    def get_queryset(self):
        color = self.kwargs['color']
        return Car.objects.filter(color=color).order_by('position')
class car_create(CreateView):
    model = Car
    form_class = CarForm
    success_url = reverse_lazy('car_list')
    context_object_name = 'cars'
    def form_valid(self, form):
        last_position = Car.objects.order_by('-position').first()
        if last_position:
            form.instance.position = last_position.position + 1
        else:
            form.instance.position = 1
        return super().form_valid(form)
class update_position(UpdateView):
    model = Car
    fields = ['position']
    http_method_names = ['post']
    def post(self, request, *args, **kwargs):
        id_lists = request.POST.getlist('id[]')
        new_positions = request.POST.getlist('order[]')
        for id_list, new_position in zip(id_lists, new_positions):
            car = Car.objects.get(pk=id_list)
            car.position = new_position
            car.save()

        return JsonResponse({'success': True})
class delete_car(DeleteView):
    model = Car
    success_url = reverse_lazy('car_list')
def swap_car(request):
    pass
def update_car(request, pk):
    pass