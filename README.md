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
        'HOST':'yourIp',
        'PORT':'yourPort',
    }
}
```
If you use mysql, you should change your `username` and `password` in <strong>setting.py</strong><br>
then go into the mysql
```
create database pamaweb
```

## Deploy project in localhost:8080
In root directory at project:<br>
- Set the database model
```
python manage.py migrate
```
- Then run
```
python manage.py runserver 0.0.0.0:8080
```
Open `localhost:8080/patient` in your browser

## The function of regular in ".recomapp/regular"
`dataRegular.py`
`regularHub.py`
`paTagController.py`

