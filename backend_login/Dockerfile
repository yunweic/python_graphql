FROM python:3.8-alpine

# install nginx
RUN apk add nginx

# forward request and error logs to docker log collector
RUN ln -sf /dev/stdout /var/log/nginx/access.log \
	&& ln -sf /dev/stderr /var/log/nginx/error.log

EXPOSE 80 443
# Finished setting up Nginx

# Make NGINX run on the foreground
RUN echo "daemon off;" >> /etc/nginx/nginx.conf
# Remove default configuration from Nginx
RUN rm /etc/nginx/conf.d/default.conf
# Copy the modified Nginx conf
COPY nginx.conf /etc/nginx/conf.d/

#create /run/nginx directory to run nginx
RUN mkdir -p /run/nginx

# Copy the base uWSGI ini file to enable default dynamic uwsgi process number
COPY uwsgi.ini /etc/uwsgi/uwsgi.ini

# install depdendency for uwsgi
RUN apk add build-base
RUN apk add linux-headers pcre-dev

# Install uWSGI
RUN pip install uwsgi

# install supervisor
RUN apk add supervisor

# Custom Supervisord config
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# install requirements for backend
COPY requirements.txt /app/requirements.txt
RUN pip3 install --upgrade pip
RUN pip3 install -r /app/requirements.txt

COPY ./src /app
WORKDIR /app

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8
ENV PYTHONUNBUFFERED=1

CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf" ]