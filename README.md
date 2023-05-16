## Passo a Passo

1- Configurar a SECRET_KEY com o auxílio dos comandos:

     python
     import secrets
     secrets.token_urlsafe(32)


2- Iniciar o app com a linha de comando:

     python3 manage.py startapp nome_do_app
  
  
3- Configurar o SuperUser:

      python manage.py createsuperuser
  
   insira um usuário e senha para configurá-lo
  
