FROM python:3.6

MAINTAINER "Jonathan Kamau <jonathan.kamau@andela.com>"

LABEL application="Episode Tracker"

ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
COPY src /code
COPY scripts/dev.sh /dev.sh
RUN sed -i 's/\r//' /dev.sh \
    && chmod +x /dev.sh
