from django.db import models
from django.conf import settings


def user_path(instance, filename):
    from random import choice
    import string
    arr = [choice(string.ascii_letters) for _ in range(8)]
    pid = ''.join(arr)
    extension = filename.split('.')[-1]
    # honux/absdfer.png
    return '%s/%s.%s' % (instance.owner.username, pid, extension)


def profile_path(instance, filename):
    extension = filename.split('.')[-1]
    # honux/profile.png
    return '{}/profile.{}'.format(instance.user.username, extension)


class Photo(models.Model):
    image = models.ImageField(upload_to=user_path)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL)
    thumbnail_image = models.ImageField(blank=True)
    comment = models.CharField(max_length=255)
    pub_date = models.DateTimeField(auto_now_add=True)


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    nickname = models.CharField(max_length=255, blank=True)
    profile_photo = models.ImageField(upload_to=profile_path, blank=True)

    def __str__(self):
        return str(self.user)
