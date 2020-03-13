FROM tbrlpld/ubuntu:latest

# Setting up NGINX
USER root
RUN aptitude install -y nginx 
# Nginx already spawns the worker processes with the non root user www-data.
# We can just run also run the main process with this user if we are not using ports below 1024
# Giving the right file permissions to the user
RUN touch /var/cache/nginx
RUN chown -R www-data:www-data /var/cache/nginx
RUN chown -R www-data:www-data /var/log/nginx
RUN chown -R www-data:www-data /var/lib/nginx
RUN chown -R www-data:www-data /etc/nginx/nginx.conf
RUN touch /run/nginx.pid
RUN chown -R www-data:www-data /run/nginx.pid
# Adding the nginx and site config
COPY nginx.conf /etc/nginx/nginx.conf
COPY site.nginx /etc/nginx/sites-enabled/site.nginx
RUN rm /etc/nginx/sites-enabled/default
# Adding the app directory
COPY src/ /app/
RUN chown -R www-data:www-data /app
WORKDIR /app
# Activating the non-root user
USER www-data

ENTRYPOINT /usr/sbin/nginx -g "daemon off;"
EXPOSE 8080