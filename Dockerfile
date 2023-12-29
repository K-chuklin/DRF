FROM python:3

WORKDIR /code

RUN pip install -r requiremetns.txt

COPY . .

# CMD ['python', 'manage.py', 'runserver']