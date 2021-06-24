
from django.urls import path
from .import views

app_name='app_tienda'

urlpatterns = [    
    path('tienda/', views.tienda, name='tienda'),

]