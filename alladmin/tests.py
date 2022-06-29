from django.test import SimpleTestCase,TestCase,Client
from django.urls import reverse,resolve
from alladmin.views import *
# Create your tests here.

class TestUrls(SimpleTestCase):
    def test_case_admindash_url(self):
        url=reverse('admindash')
        self.assertEqual(resolve(url).func,admindash)

    def test_case_addteacher_url(self):
        url=reverse('addteacher')
        self.assertEqual(resolve(url).func,addteacher)


class TestViews(TestCase):
    def setUp(self):
        self.client=Client()

    def test_admindash_GET(self):
        response=self.client.get(reverse('admindash'))
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'admindashboard.html')

    def test_addteacher_GET(self):
        response=self.client.get(reverse('addteacher'))
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'admin/addteacher.html')
