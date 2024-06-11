Steps to run project :-

1) clone project in folder

   git clone https://github.com/RahulVattaparambilGit/task_manager.git
   
3) setup virtual env and activate it(using venv or any other library)

4) switch to task_manager folder

5) install dependencies
   
   pip install -r requirements.txt
   
6) makemigrations and migrate
   
   python manage.py makemigrations
   
   python manage.py migrate
   
7) create superuser for jwt authentication(for login)

   python manage.py createsuperuser

8) run test cases(optional)

   python manage.py test

9) run server

   python manage.py runserver

Now our site will be running on localhost or http://127.0.0.1:8000/
