from django.db.models.signals import m2m_changed, post_save, pre_save
from django.dispatch import receiver
from django.core.mail import send_mail

from .settings import EMAIL_HOST_USER
from .models import Reply


@receiver(post_save, sender=Reply)
def my_handler(sender, instance, created, **kwargs):
    """Отправка письма автору объявления на новый отклик"""
    if created:
        send_mail(
            subject='Отклик на объявление',
            message=f'Вам пришел отклик от {instance.reply_author}',
            from_email=f'MMORPG <{EMAIL_HOST_USER}>',
            recipient_list=[instance.reply_ad.ad_author.email],
            fail_silently=False,
        )


@receiver(post_save, sender=Reply, dispatch_uid="reply_update_handler")
def reply_update_handler(sender, instance, created, **kwargs):
    """Отправка письма автору отклика — на реакцию автора объявлния"""
    if not created:
        if instance.reply_status is True:
            send_mail(
                subject='Ваш отклик принят',
                message=f'Ваш отклик на объявление принят автором {instance.reply_ad.ad_author}',
                from_email=f'MMORPG <{EMAIL_HOST_USER}>',
                recipient_list=[instance.reply_author.email],
                fail_silently=False,
            )
        else:
            send_mail(
                subject='Ваш отклик отклонен',
                message=f'Ваш отклик на объявление отклонен автором {instance.reply_ad.ad_author}',
                from_email=f'MMORPG <{EMAIL_HOST_USER}>',
                recipient_list=[instance.reply_author.email],
                fail_silently=False,
            )

