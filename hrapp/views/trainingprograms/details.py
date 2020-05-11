import sqlite3
from django.urls import reverse
from django.shortcuts import render, redirect
# from django.contrib.auth.decorators import login_required
from hrapp.models import TrainingProgram
# from hrapp.models import model_factory
from ..connection import Connection

def get_program(program_id):
    with sqlite3.connect(Connection.db_path) as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            p.id,
            p.title,
            p.start_date,
            p.end_date,
            p.capacity
        FROM hrapp_trainingprogram p
        WHERE p.id = ?
        """, (program_id))

        return db_cursor.fetchone()

def program_details(request, program_id):
    if request.method == 'GET':
        program = get_program(program_id)

        template = 'trainingprograms/detail.html'
        context = {
            'program': program
        }

        return render(request, template, context)
    
    if request.method == 'POST':
        form_data = request.POST

        if (
            "actual method" in form_data
            and form_data["actual_method"] == "DELETE"
        ):
            with sqlite3.connect(Connection.db_path) as conn:
                db_cursor = conn.cursor()

                db_cursor.execute("""
                DELETE FROM hrapp_trainingprogram
                WHERE id = ?
                """, (program_id))
            
            return redirect(reverse('hrapp:training'))
            