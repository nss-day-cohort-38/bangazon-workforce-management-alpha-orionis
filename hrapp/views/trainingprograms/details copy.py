# import sqlite3
# from django.urls import reverse
# from django.shortcuts import render, redirect
# # from django.contrib.auth.decorators import login_required
# from hrapp.models import TrainingProgram, Employee
# from hrapp.models import model_factory
# from ..connection import Connection

# def get_program(program_id):
#     with sqlite3.connect(Connection.db_path) as conn:
#         conn.row_factory = create_program
#         db_cursor = conn.cursor()

#         db_cursor.execute("""
#         SELECT
#             p.id,
#             p.title,
#             p.start_date,
#             p.end_date,
#             p.capacity,
#             p.employees,
#             e.first_name,
#             e.last_name,
#             etp.id,
#             etp.employee_id,
#             etp.training_program_id
#         FROM hrapp_trainingprogram p
#         JOIN hrapp_employeetrainingprogram etp ON etp.training_program_id = p.id
#         JOIN hrapp_employee e ON e.id = etp.employee_id
#         WHERE p.id = ?
#         """, (program_id,))

#         resp = db_cursor.fetchone()
#         print("resppppppp", resp)
#         return resp

# def create_program(cursor, row):
#     _row = sqlite3.Row(cursor, row)

#     tprogram = TrainingProgram()
#     tprogram.id = _row['id']
#     tprogram.title = _row['title']
#     tprogram.start_date = _row['start_date']
#     tprogram.end_date = _row['end_date']
#     tprogram.capacity = _row['capacity']

#     tprogram.employees_names = []

#     employee = Employee()
#     employee.id = _row['id']
#     employee.first_name = _row['first_name']
#     employee.last_name = _row['last_name']
#     tprogram.employees_names.append(employee)


#     return (tprogram, employee)


# def program_details(request, program_id):
#     if request.method == 'GET':
#         program = get_program(program_id)

#         program_groups = {}

#         program_groups_values = program_groups.values()

#         for (tprogram, employee) in program:
#             if tprogram.id not in program_groups:
#                 program_groups[tprogram.id] = tprogram
#                 program_groups[tprogram.id].employees_names.append(employee)
#             else:
#                 program_groups[tprogram.id].employees_names.append(employee)

#         template = 'trainingprograms/details.html'
#         context = {
#             'program_groups_values': program_groups_values
#         }

#         return render(request, template, context)
    
#     if request.method == 'POST':
#         form_data = request.POST

#         if (
#             "actual method" in form_data
#             and form_data["actual_method"] == "DELETE"
#         ):
#             with sqlite3.connect(Connection.db_path) as conn:
#                 db_cursor = conn.cursor()

#                 db_cursor.execute("""
#                 DELETE FROM hrapp_trainingprogram
#                 WHERE id = ?
#                 """, (program_id))
            
#             return redirect(reverse('hrapp:training'))
            