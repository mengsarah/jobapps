from django.db import models
import datetime


### CONSTANTS ###

# actions are not necessarily in order or all required
ACTIONS = [
    ('talk', 'talked at event'),
    ('resm', 'gave resume'),
    ('covr', 'gave cover letter'),
    ('appl', 'applied via job posting'),
    ('chln', 'coding challenge/test'),
    ('intv', 'interview')
]

ROLES = [
    ('recr', 'recruiter'),
    ('head', 'head of something'),
    ('pers', 'personal contact'),
    ('misc', 'other')
]


### MODELS FOR DATABASE ###

class Company(models.Model):
    name = models.CharField(max_length=75)
    full_name = models.CharField(max_length=200)
    about = models.TextField()
    website = models.CharField(max_length=200, blank=True)
    class Meta:
        verbose_name_plural = "companies"
    def __str__(self):
        return self.name

class JobApp(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    position = models.CharField(max_length=200, blank=True)
    # resume will just be the file name
    resume = models.CharField(max_length=200)
    cover_letter = models.TextField(blank=True)
    other_material = models.TextField(blank=True)
    notes = models.TextField(blank=True)
    def __str__(self):
        return self.position + " at " + self.company.__str__()

class JobAppStep(models.Model):
    job_app = models.ForeignKey(JobApp, on_delete=models.CASCADE)
    step = models.CharField(max_length=50, choices=ACTIONS, default='resm')
    date = models.DateField(default=datetime.date.today())
    done = models.BooleanField(default=True)
    def __str__(self):
        return self.step + " for " + self.job_app.__str__()

class Contact(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    role = models.CharField(max_length=50, choices=ROLES, default='recr')
    def __str__(self):
        return self.name + " at " + self.company.__str__()