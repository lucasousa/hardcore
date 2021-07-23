FROM python:3.6

RUN apt update

RUN mkdir /deploy/
RUN mkdir /deploy/sites/
RUN mkdir /deploy/sites/hardcore/
RUN mkdir /deploy/venvs/

RUN apt-get install -y nginx python3-dev supervisor
RUN curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
RUN python3 get-pip.py
RUN pip install virtualenv

WORKDIR /deploy/venvs
RUN virtualenv env -p python3.6

WORKDIR /deploy/sites/hardcore

COPY . .

RUN pip install -r requirements.txt

ADD services.conf /etc/nginx/conf.d/

WORKDIR /deploy/sites/hardcore/

RUN python manage.py collectstatic

RUN nginx -t -c /etc/nginx/nginx.conf

RUN service nginx restart

EXPOSE 8000

RUN python3 manage.py makemigrations
RUN python3 manage.py migrate

CMD [ "python3", "manage.py", "runserver", "0.0.0.0:8000"]