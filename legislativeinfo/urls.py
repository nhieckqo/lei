from django.urls import path
from . import views

app_name = 'legislativeinfo'
urlpatterns = [
    path('', views.OverviewLiView.as_view(), name='overview'),
    path('legislativeinfo/sort', views.event_gate, name="sort"),
    path('legislativeinfo/create',views.LegislativeInfoCreateView.as_view(),name='details_add'),
    path('legislativeinfo/<int:pk>', views.LegislativeInfoUpdateView.as_view(), name='details_edit'),
    path('legislativeinfo/<int:pk>/delete',views.LegislativeInfoDeleteView.as_view(),name="details_delete"),
]
