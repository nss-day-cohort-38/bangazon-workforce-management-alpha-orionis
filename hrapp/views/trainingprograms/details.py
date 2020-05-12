import sqlite3
from django.urls import reverse
from django.shortcuts import render, redirect
# from django.contrib.auth.decorators import login_required
from hrapp.models import TrainingProgram, Employee
from hrapp.models import model_factory
from ..connection import Connection

def get_program(program_id):
    with sqlite3.connect(Connection.db_path) as conn:
        # conn.row_factory = create_program
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            p.id,
            p.title,
            p.start_date,
            p.end_date,
            p.capacity,
            e.first_name,
            e.last_name,
            etp.id,
            etp.employee_id,
            etp.training_program_id
        FROM hrapp_trainingprogram p
        JOIN hrapp_employeetrainingprogram etp ON etp.training_program_id = p.id
        JOIN hrapp_employee e ON e.id = etp.employee_id
        WHERE p.id = ?
        """, (program_id,))

        resp = db_cursor.fetchall()
        
        tprogram = TrainingProgram()
        tprogram.employees_names = []

        for tuples in resp:
            if tprogram.id == None:
               
                tprogram.id = tuples[0]
                tprogram.title = tuples[1]
                tprogram.start_date = tuples[2]
                tprogram.end_date = tuples[3]
                tprogram.capacity = tuples[4]

                employee = Employee()
                employee.id = tuples[7]
                employee.first_name = tuples[5]
                employee.last_name = tuples[6]
                tprogram.employees_names.append(employee)
            else:
                employee = Employee()
                employee.id = tuples[7]
                employee.first_name = tuples[5]
                employee.last_name = tuples[6]
                tprogram.employees_names.append(employee)

    print("XXXXXXXXXXXXXXXX", tprogram.employees_names)
    return tprogram


def program_details(request, program_id):
    if request.method == 'GET':
        program = get_program(program_id)

        template = 'trainingprograms/details.html'
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
            