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

RUN mkdir /app/static-build

# First copy requirements.txt and peep so we can take advantage of
# docker caching.
COPY requirements.txt requirements.txt
RUN pip install --require-hashes --no-cache-dir -r requirements.txt

COPY --chown=app . /app

RUN python manage.py collectstatic --noinput
USER app

CMD ["gunicorn", "careers.wsgi:application", "--daemon". "-b", "0.0.0.0:8000", "-w 2", "--timeout", "300"]
