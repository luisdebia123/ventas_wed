
from django.urls import path
from .import views

app_name='app_blog'

urlpatterns = [    
    path('blog/', views.blog, name='blog'),
    path('categorias/<int:id>', views.categorias, name='categorias'),
]