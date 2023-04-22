FROM python:3.11
LABEL MAINTAINER="Reza Naeemi | https://radazin.com"

ENV PYTHONUNBUFFERED 1

RUN mkdir /radazin
WORKDIR /radazin

COPY . /radazin

ADD requirements.txt /radazin
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN python manage.py collectstatic --no-input

CMD ["gunicorn", "--chdir", "radazin", "--bind", "8000", "radazin.wsgi:application"]


