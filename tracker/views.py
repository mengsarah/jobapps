from django.shortcuts import render

from .models import Company, JobApp, JobAppStep, Contact
from .models import CompanyForm, JobAppForm, JobAppStepForm, ContactForm

def index(request):
    companies = Company.objects
    form_cp = CompanyForm()
    form_ja = JobAppForm()
    form_jas = JobAppStepForm()
    form_ct = ContactForm()
    forms = [form_cp, form_ja, form_jas, form_ct]
    return render(request, "tracker/index.html", {'forms': forms})