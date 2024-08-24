import os

from celery import Celery

app = Celery("tasks", broker=os.environ.get("CELERY_BROKER_URL"), backend=os.environ.get("CELERY_RESULT_BACKEND"))


@app.task
def add(x, y):
    return x + y
