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
3. Create local `.env` file (optional)
4. Run the website

## Commands

### Build

```shell
docker-compose build
```

### Create local `.env` file

You _probably_ want to add a couple local environment settings to improve local dev:

1. In the root of the project, create a file named `.env`
2. Add `ENGAGE_ROBOTS=False` - this will prevent robots from indexing the site if you happen to build locally and push to a URL that shouldn't be indexed.
3. Add `SKIP_POSTS=True` - this will avoid hitting the Wordpress API with each load of the home page (making page loads much faster). Change to `False` and re-start the server to fetch blog posts.


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
