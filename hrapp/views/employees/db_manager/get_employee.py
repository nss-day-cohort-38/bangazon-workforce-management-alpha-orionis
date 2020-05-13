import sqlite3
from ...connection import Connection
from hrapp.models import model_factory, Employee
def get_employee(employee_id):
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = model_factory(Employee)

        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT * FROM hrapp_employee e
        WHERE e.id = ?
        """, (employee_id, ))

        dataset = db_cursor.fetchone()

        return dataset

