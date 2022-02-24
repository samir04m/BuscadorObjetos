## Documentación Django 4
```
mkdir nombreCarpetaContenedora
cd nombreCarpetaContenedora
```

```
python -m venv venv_windows
```

```
venv_windows\Scripts\activate
```

```
python -m pip install --upgrade pip
```

```
pip install Django
```

```
django-admin startproject projectName
```
cd projectName

```
pip freeze > requirements.txt
```
Inicializamos repositorio: ```git init```

Y realizamos el primer commit initial state

## Creación de aplicacion
```
python manage.py startapp appName
```
Nota: Con la version 4 de django no pude hacer que me funcionara metiendola dentro de la carpeta apps. Entonces dejarla en la raiz del proyecto.

Ahora registrar la app creada en settings.py
```
INSTALLED_APPS = [
    ...
    'appName.apps.AppNameConfig',
]
```

## Instalar proyecto
```
pip install -r requirements.txt
```

```
python manage.py migrate
```

```

```

```

```

```

```

```

```

```

```

```

```