from django.urls import path
from . import views

app_name = 'main'
urlpatterns = [
    path('legislative_info', views.OverviewLiView.as_view(), name='main'),
    path('legislative_info/sort', views.event_gate, name="sort"),
    # path('legislative_info/<int:pk>', views.LegislativeInfoUpdateView.as_view(), name='details_edit'),
    path('legislative_info/<int:pk>', views.LegislativeInfoUpdateView.as_view(), name='details_edit'),

]
