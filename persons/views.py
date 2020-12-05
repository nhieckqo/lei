from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import  generic
from django.urls import reverse_lazy, reverse
from django.db import IntegrityError
from django.contrib import messages

# from django_tables2 import SingleTableView
from django_filters import FilterSet
from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin

from . import models
from . import forms
from . import tables
from . import utils


class PersonsFilter(FilterSet):

    class Meta:
        model = models.Persons
        fields = ['fullname', 'fulladdress',]


class PersonsTableView(SingleTableMixin, FilterView):
    model = models.Persons
    table_class = tables.PersonsTable
    template_name = 'persons/persons_list.html'

    filterset_class = PersonsFilter


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
        self.object.fullname = utils.get_fullname(self.object)
        self.object.fulladdress = utils.get_fulladdress(self.object)
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
        self.object.fullname = utils.get_fullname(self.object)
        self.object.fulladdress = utils.get_fulladdress(self.object)
        self.object.save()
        return super().form_valid(form)


class PersonsDeleteView(generic.DeleteView):
    model = models.Persons
    success_url = reverse_lazy('persons:persons_list')

    def delete(self, request, *args, **kwargs):
        try:
            return super().delete(request, *args, **kwargs)
        except IntegrityError as e:
            messages.add_message(request, messages.ERROR, e.args[0])
            # print (e)
            return HttpResponseRedirect(reverse_lazy('persons:persons_list'))


def event_gate(request):
    # print (request.POST)
    if request.method == "POST":
        pks = request.POST.getlist("selection")
        # selected_objects = models.Persons.objects.filter(pk__in=pks)
        if pks:
            pk = pks[0]

            if 'edit_button' in request.POST:
                return HttpResponseRedirect(reverse('persons:persons_details_edit',args=(pk,)))
            elif 'delete_button' in request.POST:
                return HttpResponseRedirect(reverse('persons:persons_details_delete',args=(pk,)))
            elif 'select_button' in request.POST:
                print (">>>", request.POST)
        else:
            if 'add_button' in request.POST:
                return HttpResponseRedirect(reverse('persons:persons_details_add'))

    return HttpResponseRedirect(reverse_lazy('persons:persons_list'))
