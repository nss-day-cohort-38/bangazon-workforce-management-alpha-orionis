import sqlite3
from django.shortcuts import render, redirect, reverse
from hrapp.models import Computer
from ..connection import Connection

def computer_list(request):
    if request.method == 'GET':
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = sqlite3.Row
            db_cursor = conn.cursor()

            db_cursor.execute("""
            SELECT
                c.id,
                c.make,
                c.purchase_date,
                c.decommission_date,
                c.manufacturer
            FROM hrapp_computer c
            """)

            all_computers = []
            dataset = db_cursor.fetchall()

            for row in dataset:
                computer = Computer()
                computer.id = row['id']
                computer.make = row['make']
                computer.purchase_date = row['purchase_date']
                computer.decommission_date = row['decommission_date']
                computer.manufacturer = row['manufacturer']

                all_computers.append(computer)

        template = 'computers/list.html'
        context = {
            'all_computers': all_computers
        }

        return render(request, template, context)

    elif request.method == 'POST':
        form_data = request.POST

        with sqlite3.connect(Connection.db_path) as conn:
            db_cursor = conn.cursor()

            db_cursor.execute("""
            INSERT INTO hrapp_computer
            (
                make, purchase_date,
                manufacturer
            )
            VALUES (?, ?, ?)
            """,
            (form_data['make'], form_data['purchaseDate'], 
            form_data['manufacturer']))

            db_cursor.execute("""
            INSERT INTO hrapp_employeecomputer
            (
                computer_id, employee_id,
                assign_date
            )
            VALUES ((SELECT c.id FROM hrapp_computer c
                     ORDER BY id DESC LIMIT 1), ?, ?)
            """,
            (form_data['employee'], 
            form_data['date']))

        return redirect(reverse('hrapp:computer_list'))