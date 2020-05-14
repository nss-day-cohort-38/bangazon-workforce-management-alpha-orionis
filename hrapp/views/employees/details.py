import sqlite3
from django.shortcuts import render, redirect, reverse
from .db_manager.get_employee import get_employee
from .db_manager.get_employee_computer import get_employee_computer
from .db_manager.get_employee_programs import get_employee_programs
from ..connection import Connection
from django.contrib.auth.decorators import login_required

@login_required
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
    
    elif request.method == 'POST':
        form_data = request.POST

        if (
            "actual_method" in form_data
            and form_data["actual_method"] == "PUT"
        ):
            with sqlite3.connect(Connection.db_path) as conn:
                db_cursor = conn.cursor()

                db_cursor.execute("""
                    UPDATE hrapp_employee
                    SET first_name = ?,
                        last_name = ?,
                        start_date = ?,
                        department_id = ?
                    WHERE id = ?
                """,
                (form_data['first_name'], form_data['last_name'], 
                form_data['start_date'], form_data['department_id'], employee_id))

            return redirect(reverse('hrapp:employee_list'))
                