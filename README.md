# Descripción
El presente código utiliza el Framework de FastApi en conjunto de AlchemySQL para generar de manera automática una base de datos en base a los modelos de tablas creadas para la API. Además, FastApi genera de manera automática el FrontEnd de la Api en base a los end points de cada controller realizado. Además, se utilizó AlchemySQL para generar una base de datos SQL lite.


## Arquitectura

El código se divide en application, core y entities.
- <b>core:</b> contiene la lógica tras el funcionamiento del código incluyendo los datos de la bases de datos, la manipulación de la base de datos y los servicios.
- <b>application:</b> contiene los controladores necesarios que aplican los routers de FastApi.
- <b>entities:</b> contiene todos los modelos necesarios que se utilizará en la aplicación.

## Tablas
Esta API administra 5 diferentes tablas presentes en la base de datos y 6 usadas para mostrar la respuesta de la API ante las peticiones del usuario o para manejar las entradas (ingreso de información) por parte del usuario. <br>
Las tablas almacenadas en la base de datos son las siguientes:
- <b>Employee:</b> Almacena la información personal y profesional del empleado.
- <b>Department:</b> Enlista los departamentos de la empresa, incluye una opción para el empleado cuyo departamento no ha sido asignado.
- <b>Position:</b> Enlista las posiciones de la empresa, incluye una opción para el empleado cuya posición no ha sido asignada.
- <b>Hard Skills:</b> Enlista las habilidades duras que la empresa necesita. Incluye una ponderación que representa su importancia dentro de la empresa.
- <b>Soft Skills:</b> Enlista las habilidades blandas que la empresa necesita. Incluye una ponderación que representa su importancia dentro de la empresa.
- <b>Employee Hard Skills:</b> Enlista las habilidades duras que posee un empleado, junto con su dominio de aquella habilidad.
- <b>Employee Soft Skills:</b> Enlista las habilidades duras que posee un empleado, junto con su dominio de aquella habilidad.

## Implementación
Los requisitos para la implementación son los siguientes:
1. Tener instalado python 3.9 o superior, y declararlo en las variables del sistema
2. Clonar o descargar el proyecto y ejecutar la siguiente línea de código en la línea de comandos:


```
    pip install pipreqs
    pipreqs /path/to/project
    ./Scripts/activate
```