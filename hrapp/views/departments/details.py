import sqlite3
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from hrapp.models import Department
from hrapp.models import Employee
from ..connection import Connection

def get_department(department_id):
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = create_employee
        db_cursor = conn.cursor()

        db_cursor.execute("""
            SELECT
                d.id,
                d.department_name,
                d.budget,
                e.first_name,
                e.last_name,
                e.id AS e_id
            FROM hrapp_department d
            LEFT JOIN hrapp_employee e
            ON e.department_id = d.id
            WHERE d.id = ?
            """, (department_id,))

        department_employees = db_cursor.fetchall()
        department = Department()
        department.employees = []
        department.name = department_employees[0]["department_name"]

        for employee in department_employees:
            department.employees.append(employee["employee"])

    return department

def create_employee(cursor, row):
    _row = sqlite3.Row(cursor, row)

    department_employee = {}
    employee = Employee()
    employee.id = _row["e_id"]
    employee.first_name = _row["first_name"]
    employee.last_name = _row["last_name"]
    department_employee["employee"] = employee
    department_employee["department_name"] = _row["department_name"]


    return department_employee

@login_required
def department_details(request, department_id):
    if request.method == 'GET':
        department = get_department(department_id)

        template = 'departments/details.html'
        context = {
            'department': department
        }

        return render(request, template, context)