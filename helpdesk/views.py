from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Ticket
from .forms import TicketForm

def index(request):
    return render(request, 'helpdesk/index.html')

def home(request):
    return render(request, 'home/home.html')