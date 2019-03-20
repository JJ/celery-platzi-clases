#!/bin/bash

sudo rabbitmqctl add_user platzi estodeberíaserunpassword        # Cambiar a una clave determinada
sudo rabbitmqctl add_vhost platzi                                # Host virtual que vamos a usar
sudo rabbitmqctl set_permissions -p platzi platzi ".*" ".*" ".*" # Permisos del usuario sobre el vhost
sudo rabbitmqctl set_user_tags platzi management                 # Calificción del usuario nuevo.
