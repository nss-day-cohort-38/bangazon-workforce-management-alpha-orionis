import sqlite3
from django.shortcuts import render
from hrapp.models import Employee
from ..connection import Connection

def employee_list(request):
    if request.method == 'GET':
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = sqlite3.Row
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

            all_employees = []
            dataset = db_cursor.fetchall()

            for row in dataset:
                employee = Employee()
                employee.id = row['employee_id']
                employee.first_name = row['first_name']
                employee.last_name = row['last_name']
                employee.start_date = row['start_date']
                employee.is_supervisor = row['is_supervisor']
                employee.department_id = row['department_id']

                all_employees.append(employee)

    template = 'employees/list.html'
    context = {
        'employees': all_employees
    }

    return render(request, template, context)
