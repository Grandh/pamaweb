# pamaweb
A simple django web for classfiy the patients

## Recommand environment 
- python 2.7+
- django 1.10+
- mysql  5.7+

## Database

You can change database in <strong>settings.py</strong>
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.yourDatabaseType',
        'NAME': 'pamaweb',
        'USER':'yourUsername',
        'PASSWORD':'yourPassword',
        'HOST':'ip',
        'PORT':'port',
    }
}
```

## Deploy project in localhost:8080
In root directory at project:
```
python manage.py runserver 0.0.0.0:8080
```

