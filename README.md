# lumbergh

[What's Deployed](https://whatsdeployed.io/s-c4g)

## Setup your environment for development

1. Get [Docker](https://www.docker.com/) and [Docker Compose](https://docs.docker.com/compose/)
2. Run Build command
3. Run the website

## Commands

### Build

```shell
docker-compose build
```

### Run the website locally
```shell
docker-compose up
```

### Run the tests

```shell
docker-compose run web ./manage.py test
```

### Sync with Greenhouse

```shell
docker-compose run web ./manage.py sync_greenhouse
```

### Close everything
```shell
docker-compose stop
```
