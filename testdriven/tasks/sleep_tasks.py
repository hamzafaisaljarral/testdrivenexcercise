from __future__ import absolute_import
import time

from celery import shared_task, Celery

app = Celery('testdrivenexcercise')
app.config_from_object('django.conf:settings')

@shared_task
def create_task(timer):
    time.sleep(int(timer))
    return True