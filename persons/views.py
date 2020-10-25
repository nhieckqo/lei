from django.shortcuts import render
from django.views import  generic

from . import models

# Create your views here.
class PersonsListView(generic.ListView):
    # model = models.Persons
    template_name = 'persons/persons_list.html'
    context_object_name = 'persons_list'

    def get_queryset(self):
        return models.Persons.objects.order_by('-p_id')[:100]

class PersonsDetailView(generic.FormView):
    model = models.Persons
    template_name = 'persons/persons_details.html'
