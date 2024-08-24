from tasks import add


def app():
    add.delay(4, 4)
    print("Task added to queue")


if __name__ == "__main__":
    app()
