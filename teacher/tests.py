from django.test import SimpleTestCase,TestCase,Client
from django.urls import reverse,resolve
from teacher.views import *
# Create your tests here.

class TestUrls(SimpleTestCase):
    def test_case_reset_url(self):
        url=reverse('reset')
        self.assertEqual(resolve(url).func,reset)




class TestViews(TestCase):
    def setUp(self):
        self.client=Client()

    def test_questionanswer_GET(self):
        response=self.client.get(reverse('reset'))
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'teacher/resetpassword.html')