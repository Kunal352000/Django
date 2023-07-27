from django.contrib import admin
from testApp.models import Employee 
# Register your models here.
# class StudentAdmin(admin.ModelAdmin):
#     list_display=['name','marks']
# admin.site.register(Student,StudentAdmin)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['eno','ename','esal','eaddr']

admin.site.register(Employee,EmployeeAdmin)