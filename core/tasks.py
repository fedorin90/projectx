from django.core.mail import send_mail

from projectx.celery import app
from .models import NewsletterSub
from .service import send_contact_info


@app.task
def contact_info_tusk(first_name, last_name, email, message):
    send_contact_info(first_name, last_name, email, message)


@app.task
def sending_spam():
    for contact in NewsletterSub.objects.all():
        send_mail(
            'You subscribe to the newsletter',
            'We will send you a lot of spam every 5 min.',
            'fedorin.mir@gmail.com',
            [contact.email],
            fail_silently=False
        )
