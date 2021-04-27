from urllib import request

from django.db.models import Q
from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from main.forms import StaffForms
from main.models import StaffModel


class StaffListView(ListView):
    template_name = 'home.html'

    def get_queryset(self):
        q = self.request.GET.get('q', '')
        return StaffModel.objects.filter(Q(name__icontains=q) | Q(info__icontains=q))


class StaffCreateView(CreateView):
    form_class = StaffForms
    template_name = 'forms.html'

    def get_success_url(self):
        return reverse('index')


class StaffUpdateView(UpdateView):
    template_name = 'forms.html'
    form_class = StaffForms
    model = StaffModel

    def get_success_url(self):
        return reverse('index')


class StaffDeleteView(DeleteView):
    model = StaffModel

    def get_success_url(self):
        return reverse('index')
