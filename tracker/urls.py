from django.urls import path

from . import views

app_name = 'tracker'

urlpatterns = [
	path('', views.index, name='index'),
	# FOR AJAX
	path('company/<int:company>', views.get_company_info, name='get_company'),
	path('contacts/<int:company>', views.get_contacts, name='get_contacts'),
	# FOR FILE OUTPUTS
	path('export/csv/steps', views.export_csv_job_app_steps, name='export_steps'),
	# FOR POST
	path('add_new', views.add_new, name='add_new'),
	path('update', views.update, name='update'),
]