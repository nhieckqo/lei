import django_tables2 as tables
from django_tables2.paginators import LazyPaginator
from django_tables2.utils import A  # alias for Accessor

from . import models


class OverviewLiTable(tables.Table):

    class Meta:
        model = models.OverviewLi
        template_name = 'django_tables2/bootstrap.html'
        paginator_class = LazyPaginator

        fields = ('res_no_full', 'approved_date', 'title', 'summary')
        order_by = 'li_id'

    selection = tables.CheckBoxColumn(accessor='pk')
    # li_id = tables.Column(verbose_name='ID')
    res_no_full = tables.Column(verbose_name='RESOLUTION NO.')
    approved_date = tables.Column(verbose_name='DATE APPROVED')
    title = tables.Column(verbose_name='TITLE')
    summary = tables.Column(verbose_name='SUMMARY')
