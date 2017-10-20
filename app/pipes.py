import os
import sys
from crawler import model
from celery import Celery
from celery import Task
from kombu import Connection
from importlib import import_module
from sqlalchemy.orm import scoped_session, sessionmaker


class SqlAlchemyTask(Task):
    """An abstract Celery Task that ensures that the connection the the
    database is closed on task completion"""
    abstract = True

    _Session = None

    def database(self):
        if self._Session is None:
            eng = model.engine()
            self._Session = scoped_session(sessionmaker(eng))
        return self._Session()

    def after_return(self, status, retval, task_id, args, kwargs, einfo):
        if self._Session is not None:
            self._Session.remove()


sys.path.append(os.getcwd())

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

broker = Celery('pipes', broker=celery_broker_url, backend=redis_url)


@broker.task(name="pipes.run_job", base=SqlAlchemyTask,
             autoretry_for=(Exception,), retry_kwargs={'max_retries': 5})
def run_job(pipe_definition, job_uuid, arguments):
    pipe_uuid = pipe_definition["uuid"]
    if job_uuid is None:
        job_uuid = pipe_definition["jobs"][0]["uuid"]
    print("running %s:%s" % (pipe_uuid, job_uuid))

    job_definition = get_job_definition(pipe_definition, job_uuid)
    defaults = job_definition["arguments"]
    print("\n\n\n\n%r\n\n%r\n\n\n\n" % (defaults, arguments))
    job_arguments = {**defaults, **arguments}
    job = get_job(job_definition)

    database = run_job.database()

    try:
        results = job.run(job_arguments, database=database)
    except RecursionError:
        print("Recursion was broken")

    next_job_definitions = get_next_job_definitions(pipe_definition, job_uuid)
    for next_job_definition in next_job_definitions:
        next_job_uuid = next_job_definition["uuid"]
        for result in results:
            que_job(pipe_definition, result, next_job_uuid)


def get_job_definition(pipe_definition, job_uuid):
    for job_definition in pipe_definition["jobs"]:
        if job_definition["uuid"] == job_uuid:
            return job_definition
    raise ParseError("No job found for %s:%s" % (pipe_definition["uuid"],
                     job_uuid))


def get_next_job_definitions(pipe_definition, job_uuid, include_recursive=True):
    definitions = []
    current_definition = get_job_definition(pipe_definition, job_uuid)
    next_job_definition = None

    for job_definition in reversed(pipe_definition["jobs"]):
        if job_definition["uuid"] == job_uuid:
            break
        else:
            next_job_definition = job_definition

    if next_job_definition is not None:
        definitions.append(next_job_definition)
    if include_recursive and current_definition.get("recursive"):
        definitions.append(current_definition)

    return definitions


def get_job(job_definition):
    job_type = job_definition["type"]
    job_module = 'jobs.%s' % job_type
    job = import_module(job_module)
    return job


def que_job(pipe_definition, arguments, job_uuid=None):
    print("queueing %s:%s" % (pipe_definition, job_uuid))
    ensure_connection()
    run_job.apply_async(
        args=(pipe_definition, job_uuid),
        kwargs={"arguments": arguments}
    )


def start(pipe_definition):
    first_job_def = pipe_definition["jobs"][0]
    job_uuid = first_job_def["uuid"]
    arguments = first_job_def["arguments"]

    que_job(pipe_definition, arguments, job_uuid)


def ensure_connection():
    conn = Connection(celery_broker_url)
    conn.ensure_connection(max_retries=10)


class ParseError(Exception):
    pass


class RecursionError(Exception):
    pass
