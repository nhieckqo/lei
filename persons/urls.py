from django.urls import path
from . import views

app_name = 'persons'
urlpatterns = [
    path('', views.PersonsTableView.as_view(),name='persons_list'),
    path('persons_details/<int:pk>',views.PersonsUpdateView.as_view(),name='persons_details'),
    path('persons_details/create',views.PersonsCreateView.as_view(),name='persons_details_create'),
    path('persons_details/<int:pk>/delete',views.PersonsDeleteView.as_view(),name="persons_details_delete"),
    path('persons_details/update',views.update_view, name='persons_update'),
]
