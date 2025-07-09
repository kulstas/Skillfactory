from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives

from celery import shared_task
import datetime

from D16_MMORPG_board.models import Advertisement, Category, User
from D16_MMORPG_board.settings import *


@shared_task
def weekly_newsletter():
    today = datetime.datetime.now()
    last_week = today - datetime.timedelta(days=7)
    ads = Advertisement.objects.filter(ad_date__gte=last_week)

    html_content = render_to_string(
        'mail/categories_weekly_email.html',
            {
                'link': SITE_URL,
                'ads': ads,
            }
        )

    msg = EmailMultiAlternatives(
            subject='Объявления за неделю',
            body='',
            from_email=DEFAULT_FROM_EMAIL,
            to=list(User.objects.filter(profile__user_subscriber=True).values_list('email', flat=True)),
        )

    msg.attach_alternative(html_content, 'text/html')
    msg.send()