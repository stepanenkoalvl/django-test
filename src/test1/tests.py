from django.test import TestCase
from django.test import Client
from django.core.urlresolvers import reverse

# Create your tests here.


class MainViewTests(TestCase):
    def test_index_view_with_first_name(self):
        response = self.client.get(reverse('test1:index'))
        self.assertContains(response, "Oleksandr", status_code=200)

    def test_index_view_with_last_name(self):
        response = self.client.get(reverse('test1:index'))
        self.assertContains(response, "Stepanenko", status_code=200)
    
    def test_index_view_with_BIO(self):
        response = self.client.get(reverse('test1:index'))
        self.assertContains(response, "???", status_code=200)

    def test_index_view_with_birth_date(self):
        response = self.client.get(reverse('test1:index'))
        self.assertContains(response, "07/19/1982", status_code=200)

    def test_index_view_with_email(self):
        response = self.client.get(reverse('test1:index'))
        self.assertContains(response, "stepanenko.alvl@gmail.com", status_code=200)

    def test_index_view_with_jabber(self):
        response = self.client.get(reverse('test1:index'))
        self.assertContains(response, "stepanenkoav@42cc.co", status_code=200) 

    def test_index_view_with_skype(self):
        response = self.client.get(reverse('test1:index'))
        self.assertContains(response, "stepanenko.alvl", status_code=200)

class MainViewDBTests(TestCase):
    def test_index_view_first_name_from_DB(self):
        response = self.client.get(reverse('test1:index'))
        self.assertQuerysetEqual(response.context['first_name'], 'Oleksandr')

    def test_index_view_last_name_from_DB(self):
        response = self.client.get(reverse('test1:index'))
        self.assertQuerysetEqual(response.context['last_name'], 'Stepanenko')

    def test_index_view_BIO_from_DB(self):
        response = self.client.get(reverse('test1:index'))
        self.assertQuerysetEqual(response.context['BIO'], '???')

    def test_index_view_birth_date_from_DB(self):
        response = self.client.get(reverse('test1:index'))
        self.assertQuerysetEqual(response.context['birth_date'], '07/19/1982')

    def test_index_view_email_from_DB(self):
        response = self.client.get(reverse('test1:index'))
        self.assertQuerysetEqual(response.context['email'], 'stepanenko.alvl@gmail.com')

    def test_index_view_jabber_from_DB(self):
        response = self.client.get(reverse('test1:index'))
        self.assertQuerysetEqual(response.context['jabber'], 'stepanenkoav@42cc.co')

    def test_index_view_skype_from_DB(self):
        response = self.client.get(reverse('test1:index'))
        self.assertQuerysetEqual(response.context['skype'], 'stepanenko.alvl')

