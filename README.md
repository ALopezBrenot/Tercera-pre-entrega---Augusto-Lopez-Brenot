# Tercera-pre-entrega---Augusto-Lopez-Brenot

# Instrucciones para clonar el repositorio y setear el proyecto 💻

## Es necesario crear una carpeta donde se va a clonar el repositorio.

Utilizando Git bash, solicitar la clonación del repositorio:

```
# git clone + https://github.com/ALopezBrenot/Tercera-pre-entrega---Augusto-Lopez-Brenot
```

Cambiar la ruta a la carpeta creada tras la clonación:

```
> cd + nombre de la carpeta
```

En la carpeta del proyecto, instalar y crear el entorno virtual:

```
> pip install virtualenv

> python -m venv venv
```

Activar el entorno virtual:

```
> venv\Scripts\activate
```
Instalar Django en el entorno virtual:

```
> pip install django
```

En el repositorio existe un archivo con las dependencias que es necesario instalar para correr el proyecto adecuadamente, el mismo puede ser leido e instalado de la siguiente manera:

```
pip install -r requirements.txt
```

El proyecto cuenta con una BBDD, para utilizarlo se deben realizar las migraciones correspondientes:

```
python manage.py migrate
```

Correr el servidor local, que permitirá visualizar las vistas:

```
python manage.py runserver
```

# Insertando registros en la Base de Datos ❗
El proyecto cuenta con tres páginas para poder ingresar registros a la base de datos. Cada sección puede ser accedida desde la barra de navegación en la parte superior.

Una vez ingresados los datos en cada campo del formulario, se debe presionar el botón **Enviar**, y será redirigido a la página de inicio.
