# Trabajando con RabbitMQ

Este directorio contiene scripts para trabajar directamente con RabbitMQ. Previo a este hay que instalar rabbitMQ. Para usarlo

* Seguir las instrucciones en [`set-up.sh`](set-up.sh) para crear usuario, clave y vhost usable desde aquí.

* Instalar las bibliotecas necesarias con

    pip install -r requirements.txt

* [`cliente.py`](cliente.py) tiene el cliente que envía mensajes, y [`trabajador.py`](trabajador.py) incluye un trabajador que lo consume. 