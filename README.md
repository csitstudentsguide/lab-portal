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

* Setting up first Django app - 
    
    1.  Open 'labPortal/labPortal/settings.py' file and add first app name 'labPortalHome' 
        in INSTALLED_APPS list.

    2.  Open 'labPortal/labPortal/urls.py' and add 'include' in line number 18     
        e.g. from django.urls import path, include

        In 'urlpatterns' list add following line after line number 21,
        e.g. path('', include('labPortalHome.urls')),

    3.  Open 'labPortal\labPortalHome\views.py' file and create a view for home page.

    4.  Create 'labPortal\labPortalHome\urls.py' file and create a url for home page.

    5.  Start Django app with ( ./manage.py runserver )

    6.  Open http://127.0.0.1:8000/ link browser to see your Django app pointing to your app now.

* Setting static files settings -

    1. Open 'labPortal/labPortal/settings.py' file and 
        add 'import  os' line, and under static files section add
        
        # Base URL to serve static files
        STATIC_URL = '/static/'
        # The absolute path to the directory where static files will be collected
        STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
        # Additional locations the staticfiles app will traverse
        STATICFILES_DIRS = [
            os.path.join(BASE_DIR, 'labPortalHome/static'),
        ]

    2.  Run database migration command 
        with ( ./manage.py makemigrations and ./manage.py migrate )

    3.  Create Django superuser with ( ./manage.py createsuperuser )

    4. Test superuser login at http://127.0.0.1:8000/admin

    5.  Collect all static files used in Django apps 
        with ( ./manage.py collectstatic )

    6.  With above commands all static files such as css, js and
        images will be stored in staticfiles folder and this folder
        will be used by WebServer to server static files.

* Setup Home page for first app - 

    1.  Store all static files required under 
        'labPortalHome/static/labPortalHome/css..js..img' folders 
        to provide app level static files.
    
    2.  Create template folder to serve HTML files
        under 'labPortalHome/templates/labPortalHome/' 
        folder to provide app level HTML templates.

    3.  Create base.html under templates folder to 
        serve repeatative HTML data like header, footer and navigation bar etc.

    4.  Create 'lab_portal_home.html' under templates folder to 
        serve as home page for your project, extend the base.html file.

        


    


    
