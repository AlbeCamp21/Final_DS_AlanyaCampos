FROM ubuntu

WORKDIR /home/api

RUN apt-get update && \
    apt-get install -y python3 python3-pip python3-venv bash

# crea el entorno virtual
RUN python3 -m venv /venv

# Copiar todo el contenido de Pregunta1 al contenedor
COPY ../Pregunta1/* ./

# activnado el entorno con bash y ejecutando comandos
CMD ["/bin/bash", "-c", "source /venv/bin/activate && pip install --upgrade pip && exec bash"]