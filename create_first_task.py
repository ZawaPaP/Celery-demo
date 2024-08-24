from tasks.tasks import add


def create_first_task():
    add.delay(4, 4)
    print("Task added to queue")


create_first_task()
