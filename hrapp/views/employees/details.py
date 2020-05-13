import sqlite3
from django.shortcuts import render, redirect, reverse
from .db_manager.get_employee import get_employee
from .db_manager.get_employee_computer import get_employee_computer
from .db_manager.get_employee_programs import get_employee_programs


def employee_details(request, employee_id):
    if request.method == "GET":
        employee = get_employee(employee_id)
        employee_computer = get_employee_computer(employee_id)
        employee_programs = [i.training_program for i in get_employee_programs(employee_id)]
        template = "employees/details.html"

        context = {
            "employee_computer": employee_computer,
            "employee_programs": employee_programs,
            "employee": employee
        }

        return render(request, template, context)