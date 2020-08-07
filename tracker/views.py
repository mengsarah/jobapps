from django.shortcuts import render
from django.forms import modelform_factory

from .models import Company, JobApp, JobAppStep, Contact

### FORM CLASSES ###
CompanyForm = modelform_factory(Company, fields='__all__')
JobAppForm = modelform_factory(JobApp, fields='__all__')
JobAppStepForm = modelform_factory(JobAppStep, fields='__all__')
ContactForm = modelform_factory(Contact, fields='__all__')

### VIEWS ###

def index(request):
    companies = Company.objects
    form_cp = CompanyForm()
    form_ja = JobAppForm()
    form_jas = JobAppStepForm()
    form_ct = ContactForm()
    forms = [form_cp, form_ja, form_jas, form_ct]
    return render(request, "tracker/index.html", {'forms': forms})