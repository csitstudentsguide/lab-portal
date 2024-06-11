# django-blog
Creating a Django Blog

For this project, I am using Ubuntu 22.04 and Python 3.10.
Current Django version is 5.0.6 and PIP version is 24.0.

* Setting Django environment - 

    1.  Check Python installation with ( python3 --version or python --version ).
    2.  Install Python3 PIP module with ( sudo apt install python3-pip ).
    3.  Check Python PIP version with ( pip -V).
    4.  Upgrdae PIP to latest version with ( python3 -m pip install --upgrade pip ).
    5.  Install Python VENV module with ( sudo apt install python3-venv )
    6.  Git clone GitHub repository, you may have created (optional).
    7.  Change directory to GitHub cloned folder with ( cd /home/user/django-blog/ )
    8.  Create a local Python virtual environment inside your project folder 
        with ( python3 -m venv .venv).
    9.  Activate your Python virtual environment with ( source .venv/bin/activate ).
    10. After successful activation, you will see (.venv) to start of your command line prompt.
    11. Check your Python and PIP version and location in your activated virtual environment
        with ( which python, which pip and python -V, pip -V ).
    12. Install Django in your virtual environment with ( pip install django ).
    13. Check Django installed properly with ( django-admin --version ).

* Creating Django project -

    1.  Create Django project with ( django-admin startproject labPortal ).
        This will create a Django project 'labPortal' in django-blog folder.
        You will see 'manage.py' file in this folder.

* Creating Django first app - 

    1.  Change directory to labPortal and create Django app in this folder 
        with ( python manage.py startapp labPortalHome ). 'labPortalHome' is your Django app.
    2.  Start Django app with ( ./manage.py runserver )
    3.  Open http://127.0.0.1:8000/ link browser to see your Django app.

    
