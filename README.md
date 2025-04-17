## Instalación del proyecto

Desde terminal nos ubicamos en la carpeta contenedora del proyecto (sin ingresar a esta):
```
python -m venv buscadorVirtualEnv
```

Activamos el virtual env:
```
buscadorVirtualEnv\Scripts\activate
```

Ingresamos a la carpeta del proyecto:
```
cd BuscadorObjetos
```

Actualizamos pip:
```
python -m pip install --upgrade pip
```

Instalación de paquetes y dependencias:
```
pip install -r requirements.txt
```

Migrar DB:
```
python manage.py migrate
```

Ejecutar servidor:
```
python manage.py runserver
```


## Creación e instalación desde cero
```
pip install Django
```

```
django-admin startproject projectName
```

```
cd projectName
```

```
pip freeze > requirements.txt
```

## Creación de aplicacion

```
python manage.py startapp appName
```

Nota: Con la version 4 de django no pude hacer que me funcionara metiendola dentro de la carpeta apps. Entonces dejarla en la raiz del proyecto.

Ahora registrar la app creada en settings.py
```
INSTALLED_APPS = [
	'appName.apps.AppNameConfig',
]
```