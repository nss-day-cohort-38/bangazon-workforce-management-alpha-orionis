from django.urls import path, include
from django.conf.urls import include
from hrapp import views
from .views import *

app_name = 'hrapp'
urlpatterns = [
    path('', home, name='home'),
    path('accounts/', include('django.contrib.auth.urls'), name='login'),
    path('logout/', logout_user, name='logout'),
    path('employees/', employee_list, name='employee_list'),
    path('employee/<int:employee_id>', employee_details, name='employee'),
    path('employee/<int:employee_id>/form/', employee_edit_form, name="employee_edit_form"),
    path('employee/form', employee_form, name='employee_form'),
    path('departments/', department_list, name='department_list'), 
    path('departments/<int:department_id>/', department_details, name='department'),
    path('departments/form/', department_form, name="department_form"),
    path('programs/', training_program_list, name='training'),
    path('programs/past', training_program_past, name='training_past'),
    path('programs/form/', training_form, name='training_form'),
    path('programs/<int:program_id>/', program_details, name='training_detail'),
    path('programs/<int:program_id>/', program_details, name='past_detail'),
    path('programs/<int:program_id>/form/', training_edit_form, name='training_edit_form'),
    path('computers/', computer_list, name='computer_list'),
    path('computers/form/', computer_form, name='computer_form'),
    path('computers/results/', search_results, name='search_results'),
    path('computers/<int:computer_id>/', computer_details, name='computer_details'),
]
