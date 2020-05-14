import sqlite3
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from ..connection import Connection
from ...models.modelfactory import model_factory
from ...models.employee import Employee

def get_employees():
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = model_factory(Employee)
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT *
        FROM hrapp_employee
        """)

        return db_cursor.fetchall()

@login_required
def computer_form(request):
    if request.method == 'GET':
        employees = get_employees()
        template = 'computers/form.html'
        context = {
            'all_employees': employees
        }

        return render(request, template, context)

