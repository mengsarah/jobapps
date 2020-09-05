from django.contrib import admin

from .models import Company, JobApp, JobAppStep, Contact

admin.site.register(Company)
admin.site.register(Contact)

# JobAppSteps should be with their corresponding JobApp
class JobAppStepInline(admin.TabularInline):
    model = JobAppStep
    extra = 0
    ordering = ['-date']

class JobAppAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Info', {'fields': ['company', 'position', 'active', 'notes']}),
        ('Materials', {
            'fields': ['resume', 'cover_letter', 'other_material'],
            'classes': ['collapse']
        }),
    ]
    inlines = [JobAppStepInline]
    ordering = ['-active']
    list_display = ('__str__', 'last_step', 'active')

admin.site.register(JobApp, JobAppAdmin)