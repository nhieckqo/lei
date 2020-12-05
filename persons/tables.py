import django_tables2 as tables
from django_tables2.paginators import LazyPaginator
from django_tables2.utils import A  # alias for Accessor

from . import models


class PersonsTable(tables.Table):
    
    class Meta:
        model = models.Persons
        template_name = 'django_tables2/bootstrap.html'
        paginator_class = LazyPaginator

        fields = ('p_id','fullname','fulladdress','pt_persons_types_code','ppst_profile_share_types_code')
        order_by = 'p_id'

    selection = tables.CheckBoxColumn(accessor='pk')
    # p_id = tables.LinkColumn('persons:persons_details_edit', args=[A("pk")], verbose_name="PID")
    p_id = tables.Column(verbose_name="PID")
    fullname = tables.Column(verbose_name="FULLNAME")
    fulladdress = tables.Column(verbose_name="FULLADDRESS")
    pt_persons_types_code = tables.Column(verbose_name="TYPE")
    ppst_profile_share_types_code = tables.Column(verbose_name="SHARE TYPE")
    # delete = tables.LinkColumn('persons:persons_details_delete', text='X', args=[A("pk")], \
    #             attrs={'a': {'class': 'btn', 'style': 'color:red;'} }, verbose_name="")
    # check = tables.TemplateColumn('<input type="checkbox" value="{{ record.pk }}" />')
