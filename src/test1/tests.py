from django.test import TestCase
from django.test import Client
from django.core.urlresolvers import reverse
from models import Somebody
from datetime import datetime

# Create your tests here.


class MainViewTests(TestCase):
    
    def setUp(self):
        Somebody.objects.create(firstName=u'Oleksandr', lastName=u'Stepanenko',
            birthDate=datetime.strptime('07/19/1982', '%m/%d/%Y'), BIO=u'???',
            email=u'stepanenko.alvl@gmail.com', jabber=u'stepanenkoav@42cc.co',
            skype=u'stepanenko.alvl')

    def test_index_view_with_first_name(self):
        response = self.client.get(reverse('test1:index'))
        self.assertContains(response, "Oleksandr")

    def test_index_view_with_last_name(self):
        response = self.client.get(reverse('test1:index'))
        self.assertContains(response, "Stepanenko")
    
    def test_index_view_with_BIO(self):
        response = self.client.get(reverse('test1:index'))
        self.assertContains(response, "???")

    def test_index_view_with_birth_date(self):
        response = self.client.get(reverse('test1:index'))
        self.assertContains(response, "07/19/1982")

    def test_index_view_with_email(self):
        response = self.client.get(reverse('test1:index'))
        self.assertContains(response, "stepanenko.alvl@gmail.com")

    def test_index_view_with_jabber(self):
        response = self.client.get(reverse('test1:index'))
        self.assertContains(response, "stepanenkoav@42cc.co") 

    def test_index_view_with_skype(self):
        response = self.client.get(reverse('test1:index'))
        self.assertContains(response, "stepanenko.alvl")

    def test_index_view_first_name_from_DB(self):
        response = self.client.get(reverse('test1:index'))
        self.assertEqual(response.context['person'].firstName, 'Oleksandr')

    def test_index_view_last_name_from_DB(self):
        response = self.client.get(reverse('test1:index'))
        self.assertEqual(response.context['person'].lastName, 'Stepanenko')

    def test_index_view_BIO_from_DB(self):
        response = self.client.get(reverse('test1:index'))
        self.assertEqual(response.context['person'].BIO, '???')

    def test_index_view_birth_date_from_DB(self):
        response = self.client.get(reverse('test1:index'))
        self.assertEqual(response.context['person'].birthDate.isoformat(), '1982-07-19')

    def test_index_view_email_from_DB(self):
        response = self.client.get(reverse('test1:index'))
        self.assertEqual(response.context['person'].email, 'stepanenko.alvl@gmail.com')

    def test_index_view_jabber_from_DB(self):
        response = self.client.get(reverse('test1:index'))
        self.assertEqual(response.context['person'].jabber, 'stepanenkoav@42cc.co')

    def test_index_view_skype_from_DB(self):
        response = self.client.get(reverse('test1:index'))
        self.assertEqual(response.context['person'].skype, 'stepanenko.alvl')

