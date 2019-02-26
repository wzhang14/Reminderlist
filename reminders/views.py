# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Reminder

def index(request):
    reminders = Reminder.objects.all()[:10]
    context = {
        'reminders': reminders
    }
    return render(request, 'index.html', context)

def details(request, id):
    reminder = Reminder.objects.get(id=id)
    context = {
        'reminder': reminder
    }
    return render(request, 'details.html', context)

def add(request):
    if(request.method == 'POST'):
        title = request.POST['title']
        text = request.POST['text']
        reminder = Reminder(title=title, text=text)
        reminder.save()
        return redirect('/reminders')
    else:
        return render(request, 'add.html')
