FROM python3.11-slime

WORKDIR / aa

COPY . . 

RUN pip3 install django

RUN python3 manage.py migrate

EXPOSE 9999

CMD ['python3','manage.py','runserver','0.0.0.0:9999']