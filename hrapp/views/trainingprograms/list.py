import sqlite3
from django.shortcuts import render, redirect, reverse
from hrapp.models import TrainingProgram
from ..connection import Connection   

def training_program_list(request):
    if request.method == 'GET':
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = sqlite3.Row
            db_cursor = conn.cursor()

            
            db_cursor.execute("""
            SELECT
                etp.id,
                etp.title,
                etp.start_date,
                etp.end_date,
                etp.capacity
            FROM hrapp_trainingprogram etp
            WHERE etp.start_date >= DATE()
            """)

            all_programs = []
            dataset = db_cursor.fetchall()

            for row in dataset:
                program = TrainingProgram()
                program.id = row['id']
                program.title = row['title']
                program.start_date = row['start_date']
                program.end_date = row['end_date']
                program.capacity = row['start_date']

                
                all_programs.append(program)

        template = 'trainingprograms/list.html'
        context = {
            'programs': all_programs
        }

        return render(request, template, context)
    
    elif request.method == 'POST':
        form_data = request.POST

        with sqlite3.connect(Connection.db_path) as conn:
            db_cursor = conn.cursor()

            db_cursor.execute("""
            INSERT INTO hrapp_trainingprogram
            (
                title, start_Date, end_date, capacity
            )
            VALUES (?, ?, ?, ?)
            """,
            (form_data['title'], form_data['start_date'], form_data['end_date'], form_data['capacity'])
            )
        return redirect(reverse('hrapp:training'))

def training_program_past(request):
    if request.method == 'GET':
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = sqlite3.Row
            db_cursor = conn.cursor()

            
            db_cursor.execute("""
            SELECT
                etp.id,
                etp.title,
                etp.start_date,
                etp.end_date,
                etp.capacity
            FROM hrapp_trainingprogram etp
            WHERE etp.start_date <= DATE()
            """)

            all_programs = []
            dataset = db_cursor.fetchall()

            for row in dataset:
                program = TrainingProgram()
                program.id = row['id']
                program.title = row['title']
                program.start_date = row['start_date']
                program.end_date = row['end_date']
                program.capacity = row['start_date']

                
                all_programs.append(program)

        template = 'trainingprograms/list.html'
        context = {
            'programs': all_programs,
            'past': True
        }

        return render(request, template, context)

