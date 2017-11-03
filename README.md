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
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'pamaweb',
        'USER':'root',
        'PASSWORD':'huang',
        'HOST':'127.0.0.1',
        'PORT':'3306',
    }
}
```

## Deploy project in localhost:8080
In root directory in project:
```
python manage.py runserver 0.0.0.0:8080
```

