# Django REST API - Tender Notices

This REST API is made to work with scrapy project. You can find the project on https://github.com/paunovaeleonora/NoticesScraper.


Authentication
 - No Authentication
 - Token Authentication follows to be implemented


URLs:
 - "api/list/" - listing all tender notices in the database
 - "api/searchByDate/" - filtering tender notices by date
 - "api/searchByNoticeId/" - filtering tender notices by Notice Number
 - "admin/" - Django Admin
 
 
 Database:
  - Sqlite3 
  - db file need to be exported from local machine or you can export from the scrapy project.
  - in DjangoREst/settings.py file add: 
         DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                 'NAME': (the absolute path to the db file from your local machine),
                }
          }


Pagination:
  - list returns maximum of 10 items per page


Installation:
  - have Python installed on your machine.
  - install virtualenv:
    pip install virtualenv
  - Git clone this repo to your PC
     git clone https://github.com/paunovaeleonora/DjangoRestApi/tree/master
    
    
Dependencies
    - cd into your the cloned repo as such:
         cd django-rest-api
    - Cset up virtual environment:
        virtualenv  venv -p python3
        source venv/bin/activate
    - Install the dependencies needed to run the app:
        pip install -r requirements.txt
    - Make migrations:
        python manage.py makemigrations
        python manage.py migrate
    - Create superuser
         python manage.py createsuperuser 
         
   Run the surver locally:
      - python manage.py runsurver
 
