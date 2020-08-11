from django.shortcuts import render, redirect
from django.forms import modelform_factory
from django.http import JsonResponse
from django.contrib import messages

from .models import Company, JobApp, JobAppStep, Contact

### FORM CLASSES ###
CompanyForm = modelform_factory(Company, fields='__all__')
JobAppForm = modelform_factory(JobApp, fields='__all__')
JobAppStepForm = modelform_factory(JobAppStep, fields='__all__')
ContactForm = modelform_factory(Contact, fields='__all__')

### VIEWS FOR AJAX ###

def get_contacts(request, company):
    if company:
        contacts = list(Contact.objects.filter(company=company).values())
        if len(contacts) == 0:
            contacts = "No contacts"
        return JsonResponse({'contacts': contacts})

### VIEWS FOR POST ###

def add_new(request):
    if request.method == 'POST':
        data = request.POST
        added = ""
        if data['form-type'] == 'type-cp':
            new_company = Company()
            new_company.name = data['name']
            new_company.full_name = data['full_name']
            new_company.about = data['about']
            new_company.website = data['website']
            added = "company: " + new_company.__str__()
            new_company.save()
        elif data['form-type'] == 'type-ja':
            new_job_app = JobApp(company_id = data['company'])
            new_job_app.position = data['position']
            new_job_app.resume = data['resume']
            new_job_app.cover_letter = data['cover_letter']
            new_job_app.other_material = data['other_material']
            new_job_app.notes = data['notes']
            added = "job app: " + new_job_app.__str__()
            new_job_app.save()
        elif data['form-type'] == 'type-jas':
            new_job_app_step = JobAppStep(job_app_id = data['job_app'])
            new_job_app_step.step = data['step']
            new_job_app_step.date = data['date']
            new_job_app_step.done = bool(data['done'])
            added = "job app step: " + new_job_app_step.__str__()
            new_job_app_step.save()
        elif data['form-type'] == 'type-ct':
            new_contact = Contact(company_id = data['company'])
            new_contact.name = data['name']
            new_contact.role = data['role']
            new_contact.email = data['email']
            new_contact.phone = data['phone']
            added = "contact: " + new_contact.__str__()
            new_contact.save()
        messages.success(request, "Added " + added)
        return redirect("tracker:index")
    # else (not a POST request)
    messages.error(request, "No data received")
    return redirect("tracker:index")

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
    job_app_steps = JobAppStep.objects.order_by('-date').order_by('-job_app')
    return render(request, "tracker/index.html", {'forms': forms, 'steps': job_app_steps})
