from django.urls import path
from .views import employee_list
from .views import project
from .views import Employeeproject



urlpatterns = [
    path('', employee_list, name='employee_list'),
    path('project/', project, name='project'),
     path('teamwork/', Employeeproject, name='teamwork'),

]

