import os
from celery import Celery
from kombu import Connection

redis_host = os.getenv("RESULT_HOST", None)
redis_port = os.getenv("RESULT_PORT", 6379)
redis_url = 'redis://%s:%s/0' % (
    redis_host,
    redis_port,
)

rabbitmq_user = os.getenv("QUEUE_USER", None)
rabbitmq_password = os.getenv("QUEUE_PASSWORD", None)
rabbitmq_host = os.getenv("QUEUE_HOST", None)
rabbitmq_port = os.getenv("QUEUE_PORT", 5672)
rabbitmq_url = 'amqp://%s:%s@%s:%s' % (
    rabbitmq_user,
    rabbitmq_password,
    rabbitmq_host,
    rabbitmq_port
)

celery_broker_url = rabbitmq_url

broker = Celery('jobs.tasks', broker=celery_broker_url, backend=redis_url)


@broker.task(name="tasks.run_job", autoretry_for=(Exception,),
             retry_kwargs={'max_retries': 5})
def run_job(pipe_definition, job_uuid, arguments):
    pipe_uuid = pipe_definition["uuid"]
    print("running %s:%s" % (pipe_uuid, job_uuid))

    job_definition = get_job_definition(pipe_definition, job_uuid)
    defaults = job_definition["arguments"]
    job_arguments = {**defaults, **arguments}
    job = get_job(job_definition)

    results = job.run(**job_arguments)

    next_job_definition = get_next_job_definition(pipe_definition, job_uuid)
    if next_job_definition is not None:
        next_job_uuid = next_job_definition["uuid"]
        for result in results:
            que_job(pipe_uuid, next_job_uuid, result)


def get_job_definition(pipe_definition, job_uuid):
    for job_definition in pipe_definition["jobs"]:
        if job_definition["uuid"] == job_uuid:
            return job_definition
    raise ParseError("No job found for %s:%s" % (pipe_definition["uuid"],
                     job_uuid))


def get_next_job_definition(pipe_definition, job_uuid):
    next_job_definition = None
    for job_definition in reversed(pipe_definition["jobs"]):
        if job_definition["uuid"] == job_uuid:
            return next_job_definition
        else:
            next_job_definition = job_definition
    raise ParseError("No next job found for %s:%s" % (pipe_definition["uuid"],
                     job_uuid))


def get_job(job_definition):
    job_type = job_definition["type"]
    job = importlib.import_module('jobs.%s' % job_type)
    return job


def que_job(self, pipe_uuid, job_uuid, arguments):
    print("queueing %s:%s" % (pipe_uuid, job_uuid))
    self.ensure_connection()
    run_job.apply_async(args=(pipe_uuid, job_uuid, arguments))


def ensure_connection(self):
    conn = Connection(celery_broker_url)
    conn.ensure_connection(max_retries=10)


class ParseError(Exception):
    pass
