FROM python:3.11.0a7-slim

WORKDIR /usr/src/app/backend

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt update && apt install -y \
    build-essential libssl-dev xvfb curl wget \
    libffi-dev libpq-dev python-dev gcc unzip nano \
    daemonize dbus-user-session fontconfig gettext \
    binutils libproj-dev git && rm -rf /var/lib/apt/lists/*

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENTRYPOINT [ "entrypoint.sh" ]