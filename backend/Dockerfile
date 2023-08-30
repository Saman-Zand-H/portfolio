FROM python:3.10.4-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app

RUN apt update \
    && apt install -y libpq-dev musl-dev gcc libffi-dev sudo \
    && rm -rf /var/lib/apt/lists/*

RUN pip install -U pip

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

ENTRYPOINT [ "sh", "entrypoint.sh" ]
