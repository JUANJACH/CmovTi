import os
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Ticket

def obtener_usuario_so():
    try:
        return os.getlogin()
    except Exception:
        return os.environ.get("USERNAME", "anonimo")

def crear_ticket(request):
    username = obtener_usuario_so()
    user, _ = User.objects.get_or_create(username=username)

    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        descripcion = request.POST.get('descripcion')
        prioridad = request.POST.get('prioridad', 'Media')  # Valor por defecto

        Ticket.objects.create(
            usuario=user,
            titulo=titulo,
            descripcion=descripcion,
            prioridad=prioridad
        )
        return redirect('lista_tickets')

    return render(request, 'tickets/crear_ticket.html', {'usuario_so': username})

def lista_tickets(request):
    username = obtener_usuario_so()
    user, _ = User.objects.get_or_create(username=username)

    tickets = Ticket.objects.filter(usuario=user)
    return render(request, 'tickets/lista_tickets.html', {
        'tickets': tickets,
        'usuario_so': username
    })
