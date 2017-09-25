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

## 安装相关依赖

```shell
pip install "celery[librabbitmq,redis,auth,msgpack]"
```


## django与celery集成

`目录结构`

- project/
    - manage.py
    - project/
        - __init__.py
        - settings.py
        - urls.py
        - celery.py

```python
# celery.py
from __future__ import absolute_import

import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

app = Celery('project')

app.config_from_object('django.conf:settings', namespace='project')

app.autodiscover_tasks()

@app.task(bind=True)
def demo_task(self):
    print('Request: {0!R}'.format(self.request))
```

`运行`

```shell
celery -A project worker -l info
```
