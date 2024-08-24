from tasks.tasks import ten_seconds_task


def create_multi_task():
    print("First task added to queue")
    ten_seconds_task.delay()
    print("Second task added to queue")
    ten_seconds_task.delay()


create_multi_task()
