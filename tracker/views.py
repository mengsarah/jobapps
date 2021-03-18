import csv, datetime
from django.shortcuts import render, redirect
from django.forms import modelform_factory
from django.forms.models import model_to_dict
from django.http import JsonResponse, HttpResponse
from django.contrib import messages

from .models import Company, JobApp, JobAppStep, Contact

### FORM CLASSES ###
from .models import JobAppStepForm
CompanyForm = modelform_factory(Company, fields='__all__')
JobAppForm = modelform_factory(JobApp, fields='__all__')
ContactForm = modelform_factory(Contact, fields='__all__')

### VIEWS FOR AJAX ###

def get_company_info(request, company):
	if company:
		info = model_to_dict(Company.objects.get(id=company))
		# now, to wrangle a potentially multiline about field into a json object...
		info["about"] = info["about"].splitlines()
		return JsonResponse(info)

def get_contacts(request, company):
	if company:
		contacts = list(Contact.objects.filter(company=company).values())
		if len(contacts) == 0:
			contacts = "No contacts"
		return JsonResponse({'contacts': contacts})

### VIEWS FOR FILE OUTPUTS ###

# Export job app steps (JobAppStep objects) as a CSV.
# Includes some information from JobApp objects (status, resume name)
# Does not include information from Company or Contact objects.
def export_csv_job_app_steps(request):
	response = HttpResponse(content_type='text/csv')
	response['Content-Disposition'] = 'attachment; filename="Job App Steps {0}.csv"'.format(datetime.date.today())

	# ordered the same as in index()
	job_app_steps = JobAppStep.objects.order_by('-job_app__active', '-job_app', '-date')

	writer = csv.writer(response)
	for jas in job_app_steps:
		done_string = "done"
		if not jas.done:
			done_string = "not done"
		step_string = jas.get_step_display()
		if jas.step == "resm":
			step_string = step_string + ": " + jas.job_app.resume
		writer.writerow([jas.job_app, step_string, jas.date, done_string])

	return response

### VIEWS FOR POST ###

def add_new(request):
	if request.method == 'POST':
		data = request.POST
		added = "" # to be put in a message
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
			# unchecked checkboxes aren't present in POST data
			if 'active' in data:
				new_job_app.active = True
			else:
				new_job_app.active = False
			added = "job app: " + new_job_app.__str__()
			new_job_app.save()
		elif data['form-type'] == 'type-jas':
			new_job_app_step = JobAppStep(job_app_id = data['job_app'])
			new_job_app_step.step = data['step']
			new_job_app_step.date = data['date']
			# unchecked checkboxes aren't present in POST data
			if 'done' in data:
				new_job_app_step.done = True
			else:
				new_job_app_step.done = False
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

def update(request):
	if request.method == 'POST':
		data = request.POST
		updated = "" # to be put in a message
		# mark a step as done
		if data["update-type"] == "step-done":
			step = JobAppStep.objects.get(id=data["step_id"])
			step.done = True
			updated = step.__str__()
			step.save()
		# mark a job app as active or inactive
		elif data["update-type"] == "job-app-active":
			job_app = JobApp.objects.get(id=data["job_app_id"])
			job_app.active = not job_app.active
			updated = job_app.__str__()
			job_app.save()
		messages.success(request, "Updated " + updated)
	# else (not a POST request)
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
	# sort job app steps by activity (active = True first),
	# then job app within activity status (most recently entered first),
	# then by date of step within each job app (most recent step first)
	# (ideally: sort by date of last step)
	job_app_steps = JobAppStep.objects.order_by('-job_app__active', '-job_app', '-date')
	return render(request, "tracker/index.html", {'forms': forms, 'steps': job_app_steps})
