# Automatic Text Summarizer

It is a user-friendly web app with responsive design.

## Features:
- Summarize both English and Nepali text.
- Summarize text via either copy-paste paragraph or URL.
- User can save summarized text.
- View top 5 trending summarized news from BBC, CNN and Nagrik News.
- Summarize pdf file to text file.

User can choose one of the following algorithms for text summarization

- Frequency Algorithm
- Sentence Matching

## Installation

1. In settings.py, replace value of SECRET_KEY with your own key.
```SECRET_KEY = os.environ.get('SECRET_KEY', '-1')```
- you can generate your secret key [here](https://www.miniwebtool.com/django-secret-key-generator/) 
2. Create database named 'text_summarizer' in MySQL via cmd or phpmyadmin.
- Edit your database credentials in following lines in settings.py
```DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'text_summarizer',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}```

3. In the terminal:
    `$ python manage.py migrate` - this will apply migrations to your local MySQL database
    `$ python manage.py createsuperuser` - this will create admin support
    * Run server as: ```$ python manage.py runserver```
