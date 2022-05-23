
from django.test import SimpleTestCase,TestCase,Client
from django.urls import reverse,resolve
from student.views import *


class TestUrls(SimpleTestCase):
    def test_case_index_url(self):
        url=reverse('teacherregister')
        self.assertEqual(resolve(url).func,register)


class TestViews(TestCase):
    def setUp(self):
        self.client=Client()

    def test_register_GET(self):
        response=self.client.get(reverse('teacherregister'))
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'reglogin/teacherregistration.html')

