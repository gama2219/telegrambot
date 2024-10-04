#celery to allow concurrency in programm processing
#with redis as a messagebroker
from celery import Celery

app = Celery('bot',
             broker='redis://localhost:6379/0',
             backend='redis://localhost:6379/1',
             include=['botintergration'])
