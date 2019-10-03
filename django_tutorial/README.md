#Projenin Olusturulmasi
django-admin.py startproject firstProject

This comment will initialize a django project in the current directory, if you wanna create django project a specified path instead of current director

use:

django-admin.py startproject firstProject {PATH}

{PATH} => /home/django_archive/lesson1


To start django project:
cd firstProject
python manage.py runserver

it will start in 8000 port defaultly, 

To set specific port:
python manage.py runserver 127.0.0.1:1234

##kill -9 $(lsof -t -i:8080)
to kill process in 8080 port
