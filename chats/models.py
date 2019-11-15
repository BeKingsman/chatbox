from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.


class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default="default.jpg", upload_to='profile_pics', blank=True)

    def __str__(self):
        return self.user.username


class Message(models.Model):
    content = models.TextField()
    sent_by = models.ForeignKey(User, on_delete=models.CASCADE,
                                related_name='kisne_bheja', null=True)
    m_sent_to = models.ForeignKey(User, on_delete=models.CASCADE,
                                  related_name='kisko_bheja', null=True)
    time = models.DateTimeField(default=datetime.now, blank=False)

    def __str__(self):
        return "By {x} to {y}".format(x=self.sent_by, y=self.m_sent_to)
