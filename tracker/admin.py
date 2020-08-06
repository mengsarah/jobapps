from django.contrib import admin

from .models import Company, JobApp, JobAppStep, Contact

admin.site.register(Company)
admin.site.register(JobApp)
admin.site.register(JobAppStep)
admin.site.register(Contact)