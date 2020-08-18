from django.urls import path

from . import views

app_name = 'tracker'

urlpatterns = [
    path('', views.index, name='index'),
    path('company/<int:company>', views.get_company_info, name='get_company'),
    path('contacts/<int:company>', views.get_contacts, name='get_contacts'),
    path('add_new', views.add_new, name='add_new'),
    path('update', views.update, name='update'),
]