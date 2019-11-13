from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.
# class UserProfileInfo(models.Model):


class Message(models.Model):
    content = models.TextField()
    sent_by = models.ForeignKey(User, on_delete=models.CASCADE,
                                related_name='kisne_bheja', null=True)
    m_sent_to = models.ForeignKey(User, on_delete=models.CASCADE,
                                  related_name='kisko_bheja', null=True)
    time = models.DateTimeField(default=datetime.now, blank=False)
