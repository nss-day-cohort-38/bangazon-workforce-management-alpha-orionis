import sqlite3
from django.shortcuts import render, redirect, reverse
from hrapp.models import Employee
from hrapp.models import model_factory
from ..connection import Connection

def employee_list(request):
    if request.method == 'GET':
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = model_factory(Employee)
            db_cursor = conn.cursor()

            db_cursor.execute("""
            select
                e.id employee_id,
                e.first_name,
                e.last_name,
                e.start_date,
                e.is_supervisor,
                e.department_id,
                d.id department_id,
                d.department_name
            from hrapp_employee e
            JOIN hrapp_department d ON e.department_id = d.id
            """)

            all_employees = db_cursor.fetchall()


        template = 'employees/list.html'
        context = {
            'employees': all_employees
        }

        return render(request, template, context)

    elif request.method == 'POST':
        form_data = request.POST

        with sqlite3.connect(Connection.db_path) as conn:
            db_cursor = conn.cursor()

            db_cursor.execute("""
            INSERT INTO hrapp_employee
            (
                first_name, last_name, start_date, 
                department_id
            )
            VALUES (?, ?, ?, ?)
            """,
            (form_data['first_name'], form_data['last_name'],
                form_data['start_date'], form_data['department_id']))

        return redirect(reverse('hrapp:employee_list'))
