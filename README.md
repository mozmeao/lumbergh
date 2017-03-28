# lumbergh

[![Build Status](https://ci.us-west.moz.works/buildStatus/icon?job=Careers/master)](https://ci.us-west.moz.works/job/Careers/master)

[What's Deployed](https://whatsdeployed.io/s-k9W)

## Commands

### Run the tests

```shell
./manage.py test
```

### Sync with Greenhouse

```shell
./manage.py sync_greenhouse
```

## University Events

To add, edit or delete university events from
the [University page](https://careers.mozilla.org/university)
edit [university_events.yml](university_events.yml) file and follow the deploy
instructions as described in Mana.

Only events with end date equal or bigger to UTC today are shown.
