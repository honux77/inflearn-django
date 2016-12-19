from django.test import TestCase

# Create your tests here.
from lotto.models import GuessNumbers
from django.utils import timezone
class GuessNumbersTestCase(TestCase):
    def test_gen_lotto_works(self):
        n = GuessNumbers(name = "test", numbers = 1, update_date = timezone.now())
        n.generate() #internally it calls __genLotto()
        print(n.lottos)
        self.assertTrue(len(n.lottos.split()) == 6)
        n.delete()
