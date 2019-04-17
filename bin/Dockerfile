FROM python:3-slim-stretch

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PIP_DISABLE_PIP_VERSION_CHECK=1

EXPOSE 8000

RUN adduser --uid 1000 --disabled-password --gecos '' --no-create-home webdev

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential wget curl sed jq && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app
RUN chown webdev /app

# First copy requirements.txt and peep so we can take advantage of
# docker caching.
COPY requirements.txt requirements.txt
RUN pip install --require-hashes --no-cache-dir -r requirements.txt
RUN pip install awscli

COPY --chown=webdev . /app
USER webdev
CMD ./bin/mirror.sh && ./bin/sync.sh && curl ${DMS}
