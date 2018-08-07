FROM python:3.6

MAINTAINER "Jonathan Kamau <jonathan.kamau@andela.com>"

LABEL application="Episode Tracker"

ENV PYTHONUNBUFFERED 1

WORKDIR /application
COPY .git /application
COPY src /application
COPY requirements.txt /application
RUN pip install -r requirements.txt
COPY scripts/test.sh /test.sh
RUN sed -i 's/\r//' /test.sh \
    && chmod +x /test.sh
