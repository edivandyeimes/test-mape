# Test MAPE

Projeto Django - Teste 

## Instalação:

1. Instalar as depências:

> pip install -r requeriments.txt


2. Edite o arquivo **settings.py**.

3. Configure a SECRET-KEY e o DEBUG:

> python3 manage.py contrib/env_gen.py 

4. Configure os arquivos estáticos.

> python3 manage.py collectstatic

5. Sincronize a base de dados:

> python3 manage.py migrate

6. Crie um usuário administrador para o sistema:

> python3 manage.py createsuperuser

7. Inicie o servidor:

> python manage.py runserver
