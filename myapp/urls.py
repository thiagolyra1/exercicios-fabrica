from django.urls import path
from .views import buscar_cep

urlpatterns = {
    path('seucep/', buscar_cep)
}
