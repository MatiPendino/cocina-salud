# cocina-salud
Website about healthy food, nutrition and cooking tricks, with a custom admin for posting new entries. Developed using Django in the backend.

## Initial configuration

1. Clone this repository:
```
git clone https://github.com/MatiPendino/cocina-salud
```
2. Create a virtual environment:
```
python -m venv venv
```
3. Active virtual environment:
```
./venv/Scripts/activate
```
4. Generate a new SECRET_KEY:

For doing this, you need to follow some steps:

- Access the Python Terminal Shell: 

To access into the Shell, you have to run the following command in the terminal of the django project:
```
(venv) python manage.py shell
```

- In the shell, import the get_random_secret() function from django.core.management.utils:

```
>>> from django.core.management.utils import get_random_secret_key
```

- Generate the secret key. In the shell, run this command:
```
>>> print(get_random_secret_key())
```

- Copy the output and close the shell:
```
>>> exit()
```

5. Replace the current SECRET_KEY for yours in CocinaSalud/settings/base.py:
```
SECRET_KEY = 'your_secret_key'
```

6. Modify the settings point:

For this, you have to open the files manage.py, CocinaSalud/asgi.py and CocinaSalud/wsgi.py to change this line:
```
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CocinaSalud.settings.production')
```

By this one:
```
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CocinaSalud.settings.local')
```

7. Install libraries:
```
(venv) pip install -r requirements.txt
```

8. Run server:
```
(venv) python manage.py runserver
```
