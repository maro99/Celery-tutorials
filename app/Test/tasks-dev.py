# Create your tasks here
from __future__ import absolute_import, unicode_literals

import datetime
import time

from celery import shared_task

# from Test.models import Task


@shared_task
def add(x, y):
    return x + y


@shared_task
def mul(x, y):
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)

# @shared_task
# def long_task():
#        start = datetime.datetime.now()
#        task = Task.objects.create(
#        start_at=datetime.datetime.now(),
#        end_at=datetime.datetime.now(),
#        )
#        time.sleep(10)
#        end = datetime.datetime.now()
#        task.start_at=start
#        task.end_at=end
#        task.save()