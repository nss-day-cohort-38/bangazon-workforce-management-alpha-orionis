import sqlite3
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from ..connection import Connection

@login_required
def computer_form(request):
    if request.method == 'GET':
        template = 'computers/form.html'
        context = {}

        return render(request, template, context)

