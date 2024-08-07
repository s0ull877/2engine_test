from celery import shared_task
from .models import Task
from time import sleep

@shared_task()
def process(task: Task):

    task.status += 1
    task.save()

    sleep(10)

    task.status += 1
    task.save()
