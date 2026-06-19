# Proyecto_POO_ValidacionCorreo

## Validación de Correo Electrónico

La aplicación valida que el correo electrónico ingresado tenga un formato correcto antes de permitir el registro de la información.

### Correos válidos

* [usuario@gmail.com](mailto:usuario@gmail.com)
* [nombre.apellido@hotmail.com](mailto:nombre.apellido@hotmail.com)
* [estudiante2026@instituto.edu.ec](mailto:estudiante2026@instituto.edu.ec)
* [cliente_empresa@dominio.com](mailto:cliente_empresa@dominio.com)

### Correos inválidos

* correo.com
* usuario@
* @gmail.com
* usuario@gmail
* usuario gmail.com
* usuario@@gmail.com

Si el correo ingresado no cumple con el formato requerido, el sistema mostrará un mensaje de error y no permitirá continuar con el proceso.

## Tecnologías Utilizadas

* Python 3
* PySide6
* Qt Designer
* Programación Orientada a Objetos (POO)
* Expresiones Regulares (Regex)

## Estructura del Proyecto

POO_Proyecto

├── Dominio

│   ├── cliente.py

│   ├── gestor_pedidos.py

│   ├── pedido_domicilio.py

│   ├── pedido_mesa.py

│   └── Servicio_Restaurante.py

├── GUI

│   └── ventana_principal.ui

├── main.py

├── README.md

└── Evidencias_ValidacionCorreo.pdf

## Ejecución del Proyecto

1. Instalar las dependencias:

pip install PySide6

2. Ejecutar la aplicación:

python main.py

## Autores

* Ambar Barrera
* Jesús Valencia
* Mayerly Reyes
* Matías Ron
* Cecilia Jacome
