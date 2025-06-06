from django.contrib import admin
from .models import Ticket

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'usuario', 'estado', 'prioridad', 'creado_en')
    list_filter = ('estado', 'prioridad')
    search_fields = ('titulo', 'usuario__username', 'descripcion')
    list_editable = ('estado', 'prioridad')
    raw_id_fields = ('usuario', 'asignado_a')