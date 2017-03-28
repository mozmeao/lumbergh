import yaml

from django.conf import settings


def load_events():
    with open(settings.EVENTS_FILE, 'a+') as fp:
        events = yaml.load(fp.read()) or []

    # Drop invalid events.
    valid_events = []

    for event in events:
        if not all([event.get('start_date'), event.get('end_date'),
                    event.get('name'), event.get('location')]):
            continue
        if event['end_date'] < event['start_date']:
            continue
        valid_events.append(event)

    return sorted(valid_events, key=lambda x: x['start_date'])


def filter_events(events, date):
    return [event for event in events if (event['end_date'] >= date)]
