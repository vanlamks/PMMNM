from django.contrib import admin
from .models import Employee
from .models import Project
from .models import EmployeeProject
# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display = [ 'employee_id','first_name', 'last_name']
    search_fields = ['last name']
admin.site.register(Employee, EmployeeAdmin);


class ProjectAdmin(admin.ModelAdmin):
    list_display = [ 'project_id', 'title']
    search_fields = ['title']
admin.site.register(Project, ProjectAdmin);

class EmployeeProjectAdmin(admin.ModelAdmin):
    list_display = [ 'employee', 'project']
    search_fields = ['employee', 'project']
admin.site.register(EmployeeProject, EmployeeProjectAdmin);