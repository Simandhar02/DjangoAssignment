Steps to setup:

1. clone project to your local machine.
2. create a virtual environment like (virtualenv venv_client_home -p python3)
3. activate your newly created virtual env using source <path to vitual env>/venv_client_home/bin/activate
4. pip install -r requirements.txt    //   install all dependencies
5. create database "test_db" locally with root/root as username/password
6. you need to set environment variable in order to run the application.
7. export ENV_PATH = /path/to/the/env/file (client_home/env/developer_env.env for local development)
8. python manage.py migrate, this will create tables in your database
9. create super user for admin panel, python manage.py createsuperuser
10. enter new credentials for login 
11. now start sever, python manage.py runserver
12. you will see, Starting development server at http://127.0.0.1:8000/
13. visit admin panel at http://127.0.0.1:8000/api/client/admin and login using the credentials of superuser


All the Best