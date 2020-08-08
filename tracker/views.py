from django.shortcuts import render
from django.forms import modelform_factory

from .models import Company, JobApp, JobAppStep, Contact

### FORM CLASSES ###
CompanyForm = modelform_factory(Company, fields='__all__')
JobAppForm = modelform_factory(JobApp, fields='__all__')
JobAppStepForm = modelform_factory(JobAppStep, fields='__all__')
ContactForm = modelform_factory(Contact, fields='__all__')

### VIEWS ###
### VIEWS FOR USERS ###

def index(request):
    # blank forms
    form_cp = CompanyForm()
    form_ja = JobAppForm()
    form_jas = JobAppStepForm()
    form_ct = ContactForm()
    forms = [
        ('Company', form_cp, 'cp'),
        ('Overall Job App', form_ja, 'ja'),
        ('Job App Step', form_jas, 'jas'),
        ('Contact', form_ct, 'ct')
    ]
    return render(request, "tracker/index.html", {'forms': forms, 'companies': Company.objects.all(),'steps': JobAppStep.objects.all()})
