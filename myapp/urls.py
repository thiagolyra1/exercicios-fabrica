from django.urls import path
from .views import buscar_cep

urlpatterns = {
    path('', buscar_cep)
}
