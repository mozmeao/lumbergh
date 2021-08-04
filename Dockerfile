FROM python:3.9-slim-buster

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PIP_DISABLE_PIP_VERSION_CHECK=1

EXPOSE 8000

RUN adduser --uid 10001 --disabled-password --gecos '' --no-create-home app

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential wget curl sed jq libfile-mimeinfo-perl && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app
RUN chown app /app

# First copy requirements.txt and peep so we can take advantage of
# docker caching.
COPY requirements.txt requirements.txt
RUN pip install --require-hashes --no-cache-dir -r requirements.txt

COPY --chown=app . /app
USER app
#RUN DEBUG=False SECRET_KEY=foo ALLOWED_HOSTS=localhost, DATABASE_URL=sqlite:/// ./manage.py collectstatic --noinput -c
RUN ./manage.py collectstatic --noinput -c
