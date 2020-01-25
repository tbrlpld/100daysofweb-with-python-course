FROM ubuntu:18.04

RUN apt-get update -y && apt-get upgrade -y
RUN apt-get install -y aptitude
RUN aptitude update -y && aptitude upgrade -y
RUN aptitude install -y -q sudo 
RUN aptitude install -y -q httpie 
RUN aptitude install -y -q fail2ban
RUN aptitude install -y -q nano

# Create a new user. This is the user with which the container is started by default.
# This user should be used for all application setup etc. 
# If you need root access, you can start the container with -U root. 
# Or for following installations/admin actions switch back to root before and back after. 
RUN useradd -s /bin/bash docker
USER docker