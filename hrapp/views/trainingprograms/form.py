import sqlite3
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# from hrapp.models import Book
# from hrapp.models import Library
# from hrapp.models import model_factory
from ..connection import Connection
# from .details import get_book

def training_form(request):
    if request.method == 'GET':
        template = 'trainingprograms/form.html'
        context = {}

        return render(request, template, context)