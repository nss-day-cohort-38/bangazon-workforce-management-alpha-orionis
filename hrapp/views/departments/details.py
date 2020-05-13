import sqlite3
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from hrapp.models import Department
from hrapp.models import Employee
# from hrapp.models import model_factory
from ..connection import Connection

def get_department(request, department_id):
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = create_department
        db_cursor = conn.cursor()

        db_cursor.execute("""
            SELECT
                d.id,
                d.department_name,
                d.budget,
                e.first_name,
                e.last_name,
                e.id
            FROM hrapp_department d
            LEFT JOIN hrapp_employee e
            ON e.department_id = d.id
            WHERE d.id = ?
            """, (department_id,))

        departments = db_cursor.fetchall()
        department_groups = {}
        department_groups_values = department_groups.values()

        for (department, employee) in departments:
            if department.id not in department_groups:
                department_groups[department.id] = department
                department_groups[department.id].employees.append(employee)

            else: 
                department_groups[department.id].employees.append(employee)

    template = 'departments/details.html'
    context = {
        'department_groups_values': department_groups_values
    }

    return render(request, template, context)

def create_department(cursor, row):
    _row = sqlite3.Row(cursor, row)

    department = Department()
    department.id = _row["id"]
    department.name = _row["department_name"]
    department.budget = _row["budget"]

    department.employees = []

    employee = Employee()
    employee.id = _row["id"]
    employee.first_name = _row["first_name"]
    employee.last_name = _row["last_name"]

    department.employee = employee

    return department


@login_required
def department_details(request, department_id):
    if request.method == 'GET':
        department = get_department(department_id)

        template = 'departments/details.html'
        context = {
            'department': department
        }

        return render(request, template, context)