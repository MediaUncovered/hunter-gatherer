from celery import Celery
import time

redis_url = 'redis://queue:6379/0'
broker = Celery('jobs.tasks', broker=redis_url)


@broker.task
def run_crawler(label, url):
    print("start")
    time.sleep(990000)
    print("end")
