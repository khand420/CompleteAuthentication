
       *1. STEP TO CREATE VIRTUAL ENVIRONMENT

1  python -m venv env/Registration
2  .\env\Registration\Scripts\Activate

3 pip install "Django==3.0.*"
4.pip freeze > requirements.txt

5 django-admin startproject Registration
6 django-admin startapp account

7 python manage.py createsuperuser khand
8.python manage.py makemigration
9.python manage.py migrate




        *2. FOR UPGRADING PIP
python -m pip install --upgrade pip




        *3. additional lacalhost(code2hell.in) in host.txt in like given below. your path-> C:\Windows\System32\drivers\etc
# localhost name resolution is handled within DNS itself.
#	127.0.0.1       localhost
#	::1             localhost

    127.0.0.1       code2hell.in





         *4. for TLS(Transport Layer Services)- it is use to https//:
install using pip 
django-extensions==2.2.5  (third paty custom extension in django)
django-extensions==2.2.5
werkzeug==0.16.0
pyOpenSSL==19.0.0

for checking ssl certificate check using command:
python manage.py runserver_plus --cert-file cert.crt


*5 RUNNING ON SERVER PORT
http://code2hell.in:8000/account/login/?next=/account/
