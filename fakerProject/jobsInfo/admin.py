from django.contrib import admin
from jobsInfo.models import * 
# Register your models here.

class hydJobsAdmin(admin.ModelAdmin):
    list_display=['date','company','title','eligibility','address','email','PhoneNumber']

admin.site.register(hydJobs,hydJobsAdmin)

class BengaluruJobsAdmin(admin.ModelAdmin):
    list_display=['date','company','title','eligibility','address','email','PhoneNumber']

admin.site.register(BengaluruJobs,BengaluruJobsAdmin)


class PuneJobsAdmin(admin.ModelAdmin):
    list_display=['date','company','title','eligibility','address','email','PhoneNumber']

admin.site.register(PuneJobs,PuneJobsAdmin)