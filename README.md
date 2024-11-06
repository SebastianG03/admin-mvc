# Descripción
Este es una api realizada con Python en FastApi y SQL lite.
Utiliza AlchemySQL para administrar y comunicarse con la bases de datos.

## Arquitectura
El código se divide en application, core y entities.
- <b>core:</b> contiene la lógica tras el funcionamiento del código incluyendo los datos de la bases de datos, la manipulación de la base de datos y los servicios.
- <b>application:</b> contiene los controladores necesarios que aplican los routers de FastApi.
- <b>entities:</b> contiene todos los modelos necesarios que se utilizará en la aplicación.

## Implementación
Los requisitos para la implementación son los siguientes:
1. Tener instalado python 3.9 o superior, y declararlo en las variables del sistema
2. Clonar o descargar el proyecto y ejecutar la siguiente línea de código en la línea de comandos:


```
    pip install pipreqs
    pipreqs /path/to/project
```