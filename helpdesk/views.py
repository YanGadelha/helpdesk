from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Ticket
from .forms import TicketForm

def index(request):
    return render(request, 'helpdesk/index.html')

@login_required
def index(request):
    tickets = Ticket.objects.filter(user=request.user)
    return render(request, 'helpdesk/index.html', {'tickets': tickets})

@login_required
def create_ticket(request):
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            return redirect('index')
    else:
        form = TicketForm()
    return render(request, 'helpdesk/ticket_form.html', {'form': form})

@login_required
def update_ticket(request, pk):
    ticket = Ticket.objects.get(pk=pk, user=request.user)
    if request.method == 'POST':
        form = TicketForm(request.POST, instance=ticket)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = TicketForm(instance=ticket)
    return render(request, 'helpdesk/ticket_form.html', {'form': form})

@login_required
def delete_ticket(request, pk):
    ticket = Ticket.objects.get(pk=pk, user=request.user)
    if request.method == 'POST':
        ticket.delete()
        return redirect('index')
    return render(request, 'helpdesk/ticket_confirm_delete.html', {'ticket': ticket})
