FROM python:3.11.2-bullseye

ENV PIP_NO_CACHE_DIR=off
ENV PIP_DISABLE_PIP_VERSION_CHECK=on
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV COLUMNS=80

RUN apt-get update \
 && apt-get install -y --force-yes \
 nano python3-pip gettext chrpath libssl-dev libxft-dev \
 libfreetype6 libfreetype6-dev  libfontconfig1 libfontconfig1-dev\
  && rm -rf /var/lib/apt/lists/*

WORKDIR /websocket

COPY ./websocket /websocket

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN chmod +x docker-entrypoint.sh

ENTRYPOINT ["sh", "/websocket/docker-entrypoint.sh"]
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]