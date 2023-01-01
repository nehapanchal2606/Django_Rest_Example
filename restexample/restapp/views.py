from django.shortcuts import render
from .models import Employee
from .form import empForm
from django.http import HttpResponse
from django.views import View
from django.views.generic import ListView, CreateView, DetailView, UpdateView
from django.urls import reverse_lazy


# Create your views here.

class addDataWithForm(ListView):
    template_name = 'add_data.html'
    model = Employee
    context = 'employees'

    def get_context_data(self, **kwargs): 
        context = super(addDataWithForm, self).get_context_data(**kwargs)
        emps = self.get_queryset()
        context['employees']= emps
        context['form'] = empForm()
        return context

    # def get(self, request):
    #     emps = self.get_queryset()
    #     context['employees']= emps
    #     form = empForm()
    #     return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = empForm(request.POST)





class createEmp(CreateView):
    model = Employee
    template_name = 'create.html'
    fields = ('firstname', 'lastname', 'email', 'password', 'phone')
    success_url = reverse_lazy('addDataWithForm')


class detailView(DetailView):
    model = Employee
    template_name = 'detail.html'
    context_object_name = 'emp'


class updateview(UpdateView):
    model = Employee
    template_name = 'update.html'
    context_object_name = 'emp'
    fields = ('firstname', 'lastname', 'email', 'password', 'phone')

    def get_success_url(self): 
        return reverse_lazy('addDataWithForm', kwargs={'pk': self.object.id})
