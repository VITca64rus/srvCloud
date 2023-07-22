import os
from celery import Celery
from celery.schedules import crontab
from app.settings import TIME_ZONE


# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')

app = Celery('app', broker=f"redis://redis:{os.getenv('REDIS_PASSWORD')}@redis:6379")

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')
app.conf.timezone = TIME_ZONE
app.conf.task_default_queue = 'default'
app.conf.beat_schedule = {

}
# Load task modules from all registered Django apps.
app.autodiscover_tasks()
