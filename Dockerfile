FROM rabbitmq:latest
LABEL version="0.1" maintainer='jjmerelo@gmail.com'

RUN apt-get update && apt-get upgrade -y && apt-get install -y python3 python3-pip 
RUN update-alternatives --install /usr/bin/python python /usr/bin/python3 1\
    && update-alternatives --install /usr/bin/pip pip /usr/bin/pip3 1
ADD requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt

WORKDIR /home/app
ADD create-user-rmq.sh cliente-con-celery.py PlatziAgenda.py PlatziTareas.py SlackComandos.py PlatziSlack.py ./
RUN mkdir data
ADD data/cursos.json data/cursos.json

CMD ./create-user-rmq.sh && celery -A PlatziTareas worker --loglevel=info & ./cliente-con-celery.py
