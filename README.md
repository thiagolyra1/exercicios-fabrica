Aqui vai ser o meu projeto para seleção de novos estagiários para a Fábrica de Software 2024.2

https://github.com/patyfil/tutorial-django

https://github.com/iuricode/padroes-de-commits

instrutuor: joaopprimo10@gmail.com

workshop-fabrica-2024.2-ThiagoLyra

settings.py -> installed_apps -> adicionarapp
settings.py -> LANGUAGE_CODE = 'pt-BR'
TIME_ZONE = 'America/Sao_Paulo'

-->> pip freeze > requirements.txt

Python 3.11.2 - Django 5.1
Os templates vão ser Django HTML. (utilizei a extensão Django no Visual Studio Code)

clonar o git: -> https://github.com/thiagolyra1/exercicios-fabrica.git

Criar o ambiente virtual: -> python -m venv venv

Ativar/Carregar o ambiente virtual: -> venv\Scripts\activate

Instalar o Django, DjangoRest Framakework e requests: -> pip install django djangorestframework requests

Instalar o Django (com a venv ativada): -> pip install django

Instalar o requests: -> pip install requests

Criar novas migrações com base nas alterações feitas nos modelos: -> python manage.py makemigrations

Aplicar e cancelar a aplicação de migrações: -> python manage.py migrate
 
Rodar o servidor: python manage.py runserver
