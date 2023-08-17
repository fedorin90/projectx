import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'projectx.settings')

app = Celery('projectx')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'sending_spam-every-5-min': {
        'task': 'core.tasks.sending_spam',
        'schedule': crontab(minute='*/5'),
    },
}
