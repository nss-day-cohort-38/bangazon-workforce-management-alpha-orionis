import sqlite3
from ...connection import Connection
from hrapp.models import model_factory, EmployeeTrainingProgram


def get_employee_programs(employee_id):
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = model_factory(EmployeeTrainingProgram)

        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT * FROM hrapp_employeetrainingprogram etp
        WHERE etp.employee_id = ?
        """, (employee_id, ))

        dataset = db_cursor.fetchall()
        program_list = []
        for item in dataset:
            program_list.append(item)
        return program_list