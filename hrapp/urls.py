from django.urls import path
from django.conf.urls import include
from hrapp import views
from .views import *

app_name = 'hrapp'
urlpatterns = [
    path('', home, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', logout_user, name='logout'),
    path('employees/', employee_list, name='employee_list'),
    path('departments/', department_list, name='department_list'), 
    path('departments/<int:department_id>/', department_details, name='department'),
    path('departments/form', department_form, name="department_form"),
    path('programs/', training_program_list, name='training'),
    path('computers/', computer_list, name='computer_list'),
    path('computers/form/', computer_form, name='computer_form'),
    # path('computers/<int:computer_id>/', computer_details, name='computer_details'),
]
