import sqlite3
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from hrapp.models import Department
from ..connection import Connection


def get_department():
    with sqlite3.connect(Connection.db_path) as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
        d.id,
        d.department_name,
        d.budget
        FROM hrapp_department d
        """)

        department = db_cursor.fetchone()
        return department


@login_required
def department_form(request):
    if request.method == 'GET':
        departments = get_department()
        template = 'departments/form.html'
        context = {
            'all_departments': departments
        }

        return render(request, template, context)
    
