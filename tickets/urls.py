from django.contrib import admin
from django.urls import path, include
from . import views

#from tickets.views import quien_soy


urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('accounts/', include('django.contrib.auth.urls')),  # Para login/logout
    ##path('quien-soy/', quien_soy),
    path('crear/', views.crear_ticket, name='crear_ticket'),
    path('mis-tickets/', views.lista_tickets, name='lista_tickets'),
    path("diagnostico/", views.diagnostico_usuario),

]

