from django.contrib import admin
from appsurvey.models import Survey
from import_export.admin import ImportExportModelAdmin
from import_export import  resources

class SurveyResource(resources.ModelResource):

    class Meta:
        model = Survey
        exclude = ('date')

class SurveyAdmin(ImportExportModelAdmin):
    resource_class = SurveyResource

# Register your models here.
admin.site.register(Survey, SurveyAdmin)
