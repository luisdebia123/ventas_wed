from django.urls import path
from .import views

app_name='app_contacto'

urlpatterns = [    
    path('contacto/', views.contacto, name='contacto'),
]