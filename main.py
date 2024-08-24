from tasks import tasks


def app():
    tasks.delay(4, 4)
    print("Task added to queue")


if __name__ == "__main__":
    app()
