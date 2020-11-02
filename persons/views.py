# from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import  generic
from django.urls import reverse_lazy
from django_tables2 import SingleTableView

from . import models
from . import forms
from . import tables


#-------------------------------------------------------------------
def get_fullname(object):
    return  (str(object.firstname).strip() if object.firstname else "") + \
        ((" "+str(object.midname).strip()) if object.midname else "") + \
        ((" "+str(object.lastname).strip()) if object.lastname else "")

def get_fulladdress(object):
    return (str(object.address_num).strip() if object.address_num else "") + \
        ((" "+str(object.address_lot).strip()) if object.address_lot else "") + \
        ((" "+str(object.address_block).strip()) if object.address_block else "") + \
        ((" "+str(object.address_street).strip()) if object.address_street else "") + \
        ((" "+str(object.address_phase).strip()) if object.address_phase else "") + \
        ((" "+str(object.address_sitio).strip()) if object.address_sitio else "") + \
        ((" "+str(object.address_brgy).strip()) if object.address_brgy else "") + \
        ((" "+str(object.address_city).strip()) if object.address_city else "") + \
        ((" "+str(object.address_province).strip()) if object.address_province else "") + \
        ((" "+str(object.address_country).strip()) if object.address_country else "") + \
        ((" "+str(object.address_zipcode).strip()) if object.address_zipcode else "")


# Create your views here.
class PersonsListView(SingleTableView):
    model = models.Persons
    table_class = tables.PersonsTable
    template_name = 'persons/persons_list.html'

class PersonsUpdateView(generic.UpdateView):
    model = models.Persons
    template_name = 'persons/persons_details.html'
    form_class = forms.PersonsForm
    success_url = reverse_lazy('persons:persons_list')

    def get_context_data(self, **kwargs):
        kwargs['submit_button_name'] = 'Update'
        context = super(PersonsUpdateView, self).get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.fullname = get_fullname(self.object)
        self.object.fulladdress = get_fulladdress(self.object)
        self.object.save()
        return super().form_valid(form)

class PersonsCreateView(generic.CreateView):
    model = models.Persons
    template_name = 'persons/persons_details.html'
    form_class = forms.PersonsForm
    success_url = reverse_lazy('persons:persons_list')

    def get_context_data(self, **kwargs):
        kwargs['submit_button_name'] = 'Create'
        context = super(PersonsCreateView, self).get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.fullname = get_fullname(self.object)
        self.object.fulladdress = get_fulladdress(self.object)
        self.object.save()
        return super().form_valid(form)

class PersonsDeleteView(generic.DeleteView):
    model = models.Persons
    success_url = reverse_lazy('persons:persons_list')
