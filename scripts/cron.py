from __future__ import print_function
import datetime

from django.core.management import call_command
from django.conf import settings

import requests
from apscheduler.schedulers.blocking import BlockingScheduler


schedule = BlockingScheduler()


class scheduled_job(object):
    """Decorator for scheduled jobs. Takes same args as apscheduler.schedule_job."""
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    def __call__(self, fn):
        job_name = fn.__name__
        self.name = job_name
        self.callback = fn
        schedule.add_job(self.run, id=job_name, *self.args, **self.kwargs)
        self.log('Registered.')
        return self.run

    def run(self):
        self.log('starting')
        try:
            self.callback()
        except Exception as e:
            self.log('CRASHED: {}'.format(e))
            raise
        else:
            self.log('finished successfully')

    def log(self, message):
        print('Clock job {0}: {1}'.format(self.name, message))


def ping_dms(function):
    """Pings Dead Man's Snitch after job completion if URL is set."""
    def _ping():
        function()
        if settings.DEAD_MANS_SNITCH_URL:
            utcnow = datetime.datetime.utcnow()
            payload = {'m': 'Run {} on {}'.format(function.__name__, utcnow.isoformat())}
            requests.get(settings.DEAD_MANS_SNITCH_URL, params=payload)
    return _ping


@scheduled_job('interval', minutes=3)
@ping_dms
def job_syncjobvite():
    call_command('syncjobvite')


def run():
    try:
        schedule.start()
    except (KeyboardInterrupt, SystemExit):
        pass
