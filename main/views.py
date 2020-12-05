from django.shortcuts import render

from django_filters import FilterSet
from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin

from . import models
from . import tables


class OverviewLiFilter(FilterSet):

    class Meta:
        model = models.OverviewLi
        fields = ['res_no_full', 'title', 'summary']


class OverviewLiView(SingleTableMixin, FilterView):
    model = models.OverviewLi
    table_class = tables.OverviewLiTable
    template_name = 'main/main.html'

    filterset_class = OverviewLiFilter
