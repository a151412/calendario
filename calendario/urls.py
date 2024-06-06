from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from calendario.views import home, listar, adicionar, create, detalhes, edit, update, delete, calendario, exit


urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('listar/', listar, name='listar'),
    path('home/', home, name='home'),
    path('adicionar/', adicionar, name='adicionar'),
    path('create/', create, name='create'),
    path('detalhes/<int:pk>/', detalhes, name='detalhes'),
    path('edit/<int:pk>/', edit, name='edit'),
    path('update/<int:pk>/', update, name='update'),
    path('delete/<int:pk>/', delete, name='delete'),
    path('', calendario, name='calendario'),
    path('logout/', exit, name='home')


]

