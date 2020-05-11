import sqlite3
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# from hrapp.models import Book
# from hrapp.models import Library
# from hrapp.models import model_factory
from ..connection import Connection
# from .details import get_book
from .details import get_program

def training_form(request):
    if request.method == 'GET':
        template = 'trainingprograms/form.html'
        context = {}

        return render(request, template, context)

def training_edit_form(request, program_id):
    if request.method == 'GET':
        program = get_program(program_id)

        template = 'trainingprograms/form.html'
        context = {
            'program': program
        }

        return render(request, template, context)

