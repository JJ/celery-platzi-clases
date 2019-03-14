sudo rabbitmqctl add_user platziu low-level-pass
sudo rabbitmqctl add_vhost platziv
sudo rabbitmqctl set_permissions -p platziv platziu ".*" ".*" ".*"
