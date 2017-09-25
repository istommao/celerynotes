from celery import Celery

app = Celery('demo', broker='amqp://guest:guest@localhost/')


@app.task
def hello():
    print('Hello celery')
    return 'Hello celery'


if __name__ == '__main__':
    result = hello.delay()
    print(result)

