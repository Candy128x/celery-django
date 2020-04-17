# Commands
	

---
## pip3 install *packages
- => pip3 install django
- => pip3 install djangorestframework

## install packages
- => cd projdemo
- => pip3 freeze > requirements.txt
- install package dependency
- => pip3 install -r requirements.txt

- => pip3 install psycopg2
- => pip3 install psycopg2-binary
- => pip3 install python-decouple

- => pip3 install celery
- => pip3 install django-celery
- => pip3 install django-celery-email


## Installing RabbitMQ on Ubuntu 18.04
- ref
>https://www.fosslinux.com/6339/how-to-install-rabbitmq-server-on-ubuntu-18-04-lts.htm

- => sudo apt-get update
- => wget -O - "https://github.com/rabbitmq/signing-keys/releases/download/2.0/rabbitmq-release-signing-key.asc" | sudo apt-key add -

- Create Rabbitmq repository file.
- => vim /etc/apt/sources.list.d/bintray.rabbitmq.list

- Add following repositories to file.
```
deb https://dl.bintray.com/rabbitmq-erlang/debian bionic erlang
deb https://dl.bintray.com/rabbitmq/debian bionic main
```

- Run Repository Update.
- => sudo apt-get update

- Install RabbitMQ Server.
- => sudo apt-get install rabbitmq-server
- Check RabbitMQ Server Status.
- => sudo systemctl status rabbitmq-server.service
- If RabbitMQ is not running, then start service with this command:
- => sudo systemctl start rabbitmq-server.service
- Enable RabbitMQ service on system boot.
- => sudo systemctl enable rabbitmq-server

---
## RabbitMQ / Celery Basic Command's
- keep the terminal session opened.
- => sudo rabbitmq-server

- if you want to run RabbitMQ in the background.
- => sudo rabbitmq-server -detached

- to know status
- => sudo rabbitmqctl status

- stop service
- => sudo rabbitmqctl stop

- restart service
- => sudo service rabbitmq-server restart

- get server info
- => cd proj_name
- => celery -A projdemo worker -l info



---
- check django version
- => django-admin --version


---
- make project
- => django-admin startproject projdemo

---
- make app
- => python3 manage.py startapp home


---
- => python3 manage.py makemigrations
- => python3 manage.py migrate


---
- create super user
- => python3 manage.py createsuperuser