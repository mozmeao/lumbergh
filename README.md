# lumbergh

[What's Deployed](https://whatsdeployed.io/s/Bcs)

Lumbergh is a Django based App for https://careers.mozilla.org. Follow the
[Setup your environment for
development](#setup-your-environment-for-development) instructions to improve
the website and fix errors.

Careers.mozilla.org website is a **static** website which is automatically
generated from its Django counterpart. If you're interested to learn how what
works and how to debug potential issues visit the [Career's Mana
Page](https://mana.mozilla.org/wiki/display/EN/careers.mozilla.org)


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
