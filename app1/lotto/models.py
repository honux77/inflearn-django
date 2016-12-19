from django.db import models
from django.utils import timezone
import random

# Create your models here.
class GuessNumbers(models.Model):
    name = models.CharField(max_length=24)
    lottos = models.CharField(max_length=120)
    numbers = models.IntegerField()
    text = models.CharField(max_length=255)
    update_date = models.DateTimeField()

    def __genLotto(self):
        self.lottos = ""
        origin = list(range(1,46))
        for _ in range(0, self.numbers):
            random.shuffle(origin)
            guess = origin[0:6]
            guess.sort()
            self.lottos += str(guess) + "\n"

    def generate(self):
        self.__genLotto()
        self.update_date = timezone.now()
        self.save()

    def __str__(self):
        return "%s %s (%s)" % (self.name, self.text, self.numbers)
