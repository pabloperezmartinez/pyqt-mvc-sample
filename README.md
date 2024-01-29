# Implementación de un MVC con PyQt5 y Psycopg2

Este proyecto es una implementación básica de un patrón Modelo-Vista-Controlador (MVC) utilizando las bibliotecas PyQt5 y Psycopg2 en Python. El MVC es un patrón de diseño de software que separa la aplicación en tres componentes principales:
el Modelo, la Vista y el Controlador, con el objetivo de lograr una estructura organizada y modular.

## Requisitos

Asegúrate de tener instaladas las siguientes bibliotecas antes de ejecutar el código:

- PyQt5: para la creación de la interfaz gráfica.
- Psycopg2: para la comunicación con una base de datos PostgreSQL.

Puedes instalar estas bibliotecas utilizando pip:

```
pip install PyQt5 psycopg2
```

## Estructura del proyecto

- controllers
  - `main_window.py`: Este archivo contiene la lógica principal de la aplicación y actúa como el Controlador.
  - `student_form.py`: Este archivo contiene la lógica de la edición de un estudiante.
- models
  - `student_model.py`: Define el Modelo de la aplicación, que se encarga de interactuar con la base de datos.
- views
  - `main_window.ui`: La interfaz gráfica se define en un archivo XML utilizando el diseñador de Qt y se compila con pyuic5 para generar lo que verá ek usuario.

## Uso

Para ejecutar la aplicación, simplemente ejecuta `main.py`:
```
python main.py
```

La aplicación mostrará una interfaz gráfica que permite interactuar con la base de datos PostgreSQL utilizando el patrón MVC.
