from django.test import TestCase
from .models import complaint
from django.utils import timezone
import datetime

class complaintTests(TestCase):

    def test_update_table(self):
        """
        """
        future_date = timezone.now().date() + datetime.timedelta(days=5)
        future_update = complaint(amend_date=future_date)
        self.assertEqual(future_date.recent_publication().False)


class MyTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up data for the whole TestCase
        cls.foo = Foo.objects.create(bar="Test")