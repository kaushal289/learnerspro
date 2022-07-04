from django.test import SimpleTestCase,TestCase,Client
from django.urls import reverse,resolve
from alladmin.views import *
# Create your tests here.

class TestUrls(SimpleTestCase):
    def test_case_studentview_url(self):
        url=reverse('studentview')
        self.assertEqual(resolve(url).func,studentview)


class TestViews(TestCase):
    def setUp(self):
        self.client=Client()

    def test_admindash_GET(self):
        response=self.client.get(reverse('studentview'))
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'admin/viewstudent.html')