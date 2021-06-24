
from django.urls import path
from .import views

app_name='app_carro'

urlpatterns = [    
    path('agregar_producto/<int:producto_id>/', views.agregar_producto, name='agregar_producto'),
    path('eliminar_producto/<int:producto_id>/', views.eliminar_producto, name='eliminar_producto'),
    path('restar_producto/<int:producto_id>/', views.restar_producto, name='restar_producto'),
    path('limpiar_carro/', views.limpiar_carro, name='limpiar_carro'),

]