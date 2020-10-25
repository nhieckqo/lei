from django.urls import path
from . import views

app_name = 'persons'
urlpatterns = [
    path('persons_list', views.PersonsListView.as_view(),name='persons_list'),
    path('persons_details',views.PersonsDetailView.as_view(),name='persons_details')
]
