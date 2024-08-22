import requests
from django.shortcuts import render, get_object_or_404, redirect
from .models import Endereco
from .forms import *

# função para consumir a api
def buscar_cep(request):
    form = EnderecoForm(request.GET or None)
    endereco = None
    
    if form.is_valid():
        cep = form.cleaned_data['cep']
        response = requests.get(f'https://viacep.com.br/ws/{cep}/json')
        
        if response.status_code == 200:
            dados_endereco = response.json()
            endereco = Endereco.objects.create(
                cep = cep,
                logradouro = dados_endereco.get('logradouro'),
                bairro = dados_endereco.get('bairro'),
                localidade = dados_endereco.get('localidade'),
                uf = dados_endereco.get('uf')                
        )
    return render(request, 'index.html', {'form': form, 'endereco': endereco} )