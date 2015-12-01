#!/usr/bin/env python
import subprocess

from apscheduler.events import EVENT_ALL
from apscheduler.schedulers.blocking import BlockingScheduler


def syncjobvite():
    print('Running syncjobvite')
    subprocess.call('python manage.py syncjobvite', shell=True)


if __name__ == '__main__':
    scheduler = BlockingScheduler()
    scheduler.add_job(syncjobvite, 'interval', minutes=10, max_instances=1, misfire_grace_time=None)

    print('Press Ctrl+C to exit')

    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        pass
