from django.test import TestCase
from django.contrib.auth.models import User
from app.models import Redirect


# Create your tests here.
class RedirectTests(TestCase):        
    def setUp(self):
        user = User.objects.create_user('tmob', 'tmob@gmail.com', 'tm123456')
        user.save()
        self.client = self.client_class()
        self.client.login(username=user.username, password='tm123456')

        self.redirect1 = Redirect.objects.create(key='abcde', url='miurl', active=True)
        self.redirect2 = Redirect.objects.create(key='abcdef', url='miurl2', active=True)
        self.redirect3 = Redirect.objects.create(key='abcdeg', url='miurl3', active=False)
    
    def test_viewRedirect(self):
        path = "/redirect/abcde/"
        response = self.client.get(path)
        self.assertEqual(response.status_code, 200)
        json = response.json()
        self.assertEqual(json['key'], self.redirect1.key)
        self.assertEqual(json['url'], self.redirect1.url)
    
    def test_not_viewRedirect(self):
        # active in false, then the status_code is 400 because not exist the key in cache
        path = "/redirect/abcdeg/"
        response = self.client.get(path)
        self.assertEqual(response.status_code, 400)


        
