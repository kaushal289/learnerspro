from django.test import SimpleTestCase,TestCase,Client
from django.urls import reverse,resolve
from teacher.views import *
# Create your tests here.

class TestUrls(SimpleTestCase):
    def test_case_addsubject_url(self):
        url=reverse('addsubject')
        self.assertEqual(resolve(url).func,addsubject)


class TestViews(TestCase):
    def setUp(self):
        self.client=Client()

    def test_register_GET(self):
        response=self.client.get(reverse('addsubject'))
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'teacher/addsubject.html')