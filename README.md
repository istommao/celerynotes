# celerynotes
celery notes

`demo`

```python
from celery import Celery

app = Celery('demo', broker='amqp://guest@localhost//')


@app.task
def hello():
    return 'Hello celery'
```