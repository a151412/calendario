from django.contrib import admin
from django.conf.urls.static import static
from django.urls import include, path
from calendario.views import home, listar, adicionar, create, detalhes, edit, update, delete, calendario, exit

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('calendario.urls')),

]

