FROM python:3.6

MAINTAINER "Jonathan Kamau <jonathan.kamau@andela.com>"

LABEL application="Episode Tracker"

ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
COPY .git /code
COPY src /code
RUN pip install -r requirements.txt
COPY scripts/test.sh /test.sh
RUN sed -i 's/\r//' /test.sh \
    && chmod +x /test.sh
