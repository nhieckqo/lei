from django.shortcuts import render
from django.views.generic import DeleteView
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect

from django_filters import FilterSet
from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin

from extra_views import CreateWithInlinesView, UpdateWithInlinesView, InlineFormSetFactory, NamedFormsetsMixin

from . import models
from . import tables
from . import forms


class OverviewLiFilter(FilterSet):

    class Meta:
        model = models.OverviewLi
        fields = ['res_no_full', 'title', 'summary']


class OverviewLiView(SingleTableMixin, FilterView):
    model = models.OverviewLi
    table_class = tables.OverviewLiTable
    template_name = 'main/main.html'

    filterset_class = OverviewLiFilter

# class LegislativeInfoUpdateView(UpdateView):
#     model = models.LegislativeInfo
#     template_name = "main/details.html"
#     form_class = forms.LegislativeInfoForm
#     success_url = reverse_lazy('main:main')
#
#     def get_context_data(self, **kwargs):
#         kwargs['submit_button_name'] = 'Update'
#         context = super(LegislativeInfoUpdateView, self).get_context_data(**kwargs)
#         return context

class LegPresidedOverByInline(InlineFormSetFactory):
    # model_presiding_officers = models.CfgPresidingOfficers
    model = models.LegPresidedOverBy
    # fields = ['presided_over_by_name', 'presided_over_by_designation']
    form_class = forms.LegPresidedOverByForm

    # pob_name = model_presiding_officers.objects.get(pk=1)
    initial = [
                # {'presided_over_by_name': pob_name, 'presided_over_by_designation': 'Vice Mayor'},
                # {'li_li_po': 1}
                ]
    factory_kwargs = {'extra': 1, 'max_num': None,
                      'can_order': False, 'can_delete': True}
    # formset_kwargs = {'auto_id': 'my_id_%s'}

class LegAttendeesInline(InlineFormSetFactory):
    model = models.LegAttendees
    form_class = forms.LegAttendeesForm
    # prefix = 'attendees-form'
    factory_kwargs = {'extra': 1, 'max_num': None,
                      'can_order': False, 'can_delete': True}


class LegCertifiedByInline(InlineFormSetFactory):
    model = models.LegCertifiedBy
    form_class = forms.LegCertifiedByForm
    factory_kwargs = {'extra': 1, 'max_num': None,
                      'can_order': False, 'can_delete': True}


class LegislativeInfoUpdateView(NamedFormsetsMixin, UpdateWithInlinesView):
    model = models.LegislativeInfo
    inlines = [LegPresidedOverByInline, LegAttendeesInline, LegCertifiedByInline]
    inlines_names = ['LegPresidedOverBy', 'LegAttendees', 'LegCertifiedBy']
    # fields = ['record_no', 'series', 'approved_date', 'title', 'summary', 'body_text',]
    template_name = 'main/details.html'
    success_url = reverse_lazy('main:main')
    form_class = forms.LegislativeInfoForm

    def get_context_data(self, **kwargs):
        kwargs['submit_button_name'] = 'Update'
        context = super(LegislativeInfoUpdateView, self).get_context_data(**kwargs)
        return context


class LegislativeInfoCreateView(NamedFormsetsMixin, CreateWithInlinesView):
    model = models.LegislativeInfo
    template_name = 'main/details.html'
    inlines = [LegPresidedOverByInline, LegAttendeesInline, LegCertifiedByInline]
    inlines_names = ['LegPresidedOverBy', 'LegAttendees', 'LegCertifiedBy']
    form_class = forms.LegislativeInfoForm
    success_url = reverse_lazy('main:main')

    def get_context_data(self, **kwargs):
        kwargs['submit_button_name'] = 'Create'
        context = super(LegislativeInfoCreateView, self).get_context_data(**kwargs)
        return context


class LegislativeInfoDeleteView(DeleteView):
    model = models.LegislativeInfo
    success_url = reverse_lazy('main:main')

    def delete(self, request, *args, **kwargs):
        try:
            return super().delete(request, *args, **kwargs)
        except IntegrityError as e:
            messages.add_message(request, messages.ERROR, e.args[0])
            # print (e)
            return HttpResponseRedirect(reverse_lazy('main:main'))


def event_gate(request):

    if request.method == 'POST':
        pks = request.POST.getlist('selection')

        if pks:
            pk = pks[0]

            if 'edit_button' in request.POST:
                return HttpResponseRedirect(reverse('main:details_edit', args=(pk,)))
            elif 'delete_button' in request.POST:
                return HttpResponseRedirect(reverse('main:details_delete',args=(pk,)))

        else:
            if 'add_button' in request.POST:
                return HttpResponseRedirect(reverse('main:details_add'))

    return HttpResponseRedirect(reverse_lazy('main:main'))
