FROM tbrlpld/ubuntu:latest

USER root
# Install Python
RUN apt-get install -y build-essential 
RUN aptitude install -y git
RUN aptitude install -y python3-pip
RUN aptitude install -y python3-dev
RUN aptitude install -y python3-venv

# Adding the app and venv directory and changing owner ship to the docker user
RUN mkdir /app
RUN chown -R docker:docker /app
RUN mkdir /venv
RUN chown -R docker:docker /venv

# From here on nothing needs root privileges anymore
USER docker
WORKDIR /app
RUN python3 -m venv /venv
RUN /venv/bin/python -m pip install -U pip setuptools
# The requirements need to be available before the whole source is copied, because the source will change frequently, while the requirements might stay the same for longer periods during development.
COPY ./src/requirements.txt /app  
RUN /venv/bin/python -m pip install -r requirements.txt

COPY ./src/ /app

ENTRYPOINT /venv/bin/python app.py
EXPOSE 7007