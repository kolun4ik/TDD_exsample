from django.test import TestCase

# Create your tests here.

class SmokeTest(TestCase):
    """Тест на токсичность"""

    def test_bad_math(self):
        """Тест: неправильные математические расчеты"""
        self.assertEqual(1+1, 3)