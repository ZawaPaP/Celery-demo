import logging
import time

from init_logging import init_logging
from tasks.celery_app import app

init_logging()
logger = logging.getLogger("tasks")


@app.task
def add(x, y):
    logger.info(f"Adding {x} and {y}")
    return x + y


@app.task
def ten_seconds_task():
    time.sleep(10)
    logger.info("Task completed")
    return "Task completed"
