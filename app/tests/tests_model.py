import datetime
from django.test import TestCase
from app.models import Redirect

# Create your tests here.
class RedirectTests(TestCase):
    def setUp(self):
        self.redirect1 = Redirect.objects.create(key='abcde', url='miurl', active=True)
        self.redirect2 = Redirect.objects.create(key='abcdef', url='miurl2', active=True)
        self.redirect3 = Redirect.objects.create(key='abcdeg', url='miurl3', active=False)
    
    def test_create(self):
        abcde = Redirect.objects.get(key="abcde")
        self.assertEqual(abcde.key, self.redirect1.key)
    
    def test_dates(self):
        abcde = Redirect.objects.get(key="abcde")
        self.assertEqual(str(abcde.created_at), str(datetime.date.today()))
    
    def test_update(self):
        Redirect.objects.filter(key='abcde').update(active=False)
        updated1=Redirect.objects.get(key="abcde")
        self.assertEqual(updated1.active, not(self.redirect1.active))
        self.assertEqual(str(updated1.updated_at), str(datetime.date.today()))
