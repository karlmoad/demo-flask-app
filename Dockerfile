FROM python:3.9.5

RUN apt-get update
RUN apt-get install -y nginx supervisor

RUN pip3 install uwsgi

# Setup flask application
RUN mkdir -p /api_service
COPY /api/ /api_service
COPY requirements.txt /api_service/requirements.txt
RUN pip3 install -r /api_service/requirements.txt

# Create nginx user
RUN useradd --no-create-home nginx

# Setup nginx
RUN rm /etc/nginx/sites-enabled/default
RUN rm -r /root/.cache

COPY nginx.conf /etc/nginx/
COPY flask-nginx.conf /etc/nginx/conf.d/
COPY uwsgi.ini /etc/uwsgi/
COPY supervisord.conf /etc/supervisor/

WORKDIR /api_service

CMD ["/usr/bin/supervisord"]


