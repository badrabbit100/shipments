FROM python:3.7-alpine3.9

ENV PYTHONUNBUFFERED 1
ENV PROJECT_ROOT /project
ENV SRC_DIR $PROJECT_ROOT/src

RUN apk update && \
    apk upgrade && \
    apk --no-cache add py3-virtualenv \
                       postgresql-dev gcc musl-dev python3-dev \
                       zlib-dev jpeg-dev \
                       postgresql-client && \
    pip install --upgrade pip && \
    pip install wheel pipenv

RUN mkdir $PROJECT_ROOT
COPY Pipfile $PROJECT_ROOT
COPY Pipfile.lock $PROJECT_ROOT
COPY ./src $SRC_DIR

WORKDIR $PROJECT_ROOT

RUN pipenv install --deploy --system --dev

ENV PYTHONPATH $SRC_DIR:$SRC_DIR/fogstream_site

EXPOSE 80

ENV GUNICORN_CONF /gunicorn.conf.py
COPY ./docker/gunicorn.conf.py $GUNICORN_CONF

COPY ./docker/run_django.sh /run_django.sh
RUN chmod +x /run_django.sh

COPY ./docker/run_tests.sh /run_tests.sh
RUN chmod +x /run_tests.sh

CMD ["/run_django.sh"]
