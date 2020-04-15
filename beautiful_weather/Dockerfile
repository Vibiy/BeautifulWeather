FROM python:3.7-alpine
ENV PYTHONUNBUFFERED 1
RUN apk update \
    && apk add --no-cache \
        gcc \
        musl-dev \
        libgcc \
        build-base \
        python-dev \
        git
RUN mkdir /beautiful_weather
WORKDIR /beautiful_weather
COPY . /beautiful_weather/
RUN pip install -r requirements.txt
RUN chmod +x entrypoint.sh
