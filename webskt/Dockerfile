# FROM python:3.8-slim-buster

# WORKDIR /app

# COPY requirements.txt  requirements.txt

# RUN pip install -r requirements.txt

# COPY . .

# CMD ["python","manage.py","runserver","0.0.0.0:8000"]



FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN pip freeze > requirements.txt
COPY . /code/
