from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image
from django.db.models.signals import post_save
import mimetypes


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    user_avatar = models.ImageField(default='default.jpg', upload_to='img/users/', blank=True)
    user_subscriber = models.BooleanField(default=False, blank=True, null=True)

    def __str__(self):
        return self.user.username

    def post_user_created_signal(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    post_save.connect(post_user_created_signal, sender=User)

    def save(self, *args, **kwargs):
        """save the profile first"""
        super().save(*args, **kwargs)

        """resize the image"""
        img = Image.open(self.user_avatar.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            """create a thumbnail"""
            img.thumbnail(output_size)
            """overwrite the larger image"""
            img.save(self.user_avatar.path)


class Category(models.Model):
    category_name = models.CharField(max_length=64, unique=True)
    category_desc = models.TextField(blank=True)

    def __str__(self):
        return self.category_name.title()

    def ads_count(self):
        return Advertisement.objects.filter(ad_category_id=self.pk).count()


class Advertisement(models.Model):
    ad_title = models.CharField(max_length=74, db_index=True, unique=True)
    ad_text = models.TextField()
    ad_date = models.DateField(auto_now_add=True)
    ad_category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, related_name='ads')
    ad_author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='author')
    ad_upload = models.FileField(upload_to='uploads/', null=True, blank=True)
    ad_status = models.BooleanField(default=True)

    class Meta:
        ordering = ['-ad_date']

    def __str__(self):
        return f'{self.ad_title.title()}: {self.ad_text[:20]}'

    def preview(self):
        return self.ad_title[0:124] + "..."

    def get_absolute_url(self):
        return reverse('ad_detail', args=[str(self.id)])

    def reply_count(self):
        return Reply.objects.filter(reply_ad=self.pk).count()

    def output_file(self):
        return mimetypes.guess_type(self.ad_upload.url)[0]


class Reply(models.Model):
    reply_ad = models.ForeignKey(Advertisement, on_delete=models.CASCADE, related_name='replies')
    reply_author = models.OneToOneField(User, on_delete=models.CASCADE, related_name='replies_authors', null=True, unique=True)
    reply_text = models.TextField(blank=True)
    reply_status = models.BooleanField(blank=True, null=True)
    reply_date = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['reply_date']

    def __str__(self):
        return f'Отклик {self.reply_text} от {self.reply_author}'


class OneTimeCode(models.Model):
    """Активация по коду на Email"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    code = models.CharField(max_length=6)
