from django.db import models
from django.utils import timezone
import random

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=256)
    text = models.TextField()
    bonus = models.CharField(max_length=24)
    update_date = models.DateTimeField(default = timezone.now)

    def publish(self):
        self.update_date = timezone.now()
        self.bonus = self.lotto()
        self.save()

    def lotto(self):
        a = list(range(1,46))
        random.shuffle(a)
        return a[0:6]

    def __str__(self):
        return "%s: %s" % (self.title, self.bonus)
