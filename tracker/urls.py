from django.urls import path

from . import views

app_name = 'tracker'

urlpatterns = [
    path('', views.index, name='index'),
    path('contacts/<int:company>', views.get_contacts, name='get_contacts'),
    path('add_new', views.add_new, name='add_new'),
]