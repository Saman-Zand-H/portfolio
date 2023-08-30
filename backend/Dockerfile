FROM python:3.12-rc-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app

RUN apt update \
    && apt install -y libpq-dev musl-dev gcc libffi-dev sudo \
    && rm -rf /var/lib/apt/lists/*

RUN useradd -ms /bin/bash server && usermod -G sudo server
USER server

ENV PATH="/home/server/.local/bin:${PATH}"

RUN pip install -U pip

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

ENTRYPOINT [ "sh", "entrypoint.sh" ]
