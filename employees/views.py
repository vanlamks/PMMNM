from django.shortcuts import render
from .models import Employee
from .models import Project
from .models import EmployeeProject

def employee_list(request):
    employees = Employee.objects.all()  # Lấy tất cả nhân viên từ database
    return render(request, 'employee_list.html', {'employees': employees})

def project(request):
    projects = Project.objects.all()  # Đúng model cần lấy
    return render(request, 'employee/project.html', {'projects': projects})  # Truyền đúng tên biến



def Employeeproject(request):
    employees_project = EmployeeProject.objects.all()  # Lấy danh sách nhân viên và dự án
    return render(request, 'employee/teamwork.html', {'employee_projects': employees_project})  # Truyền đúng tên biến
