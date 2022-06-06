from django.test import SimpleTestCase,TestCase,Client
from django.urls import reverse,resolve
from student.views import *
# Create your tests here.

class TestUrls(SimpleTestCase):
    def test_case_questionanswer_url(self):
        url=reverse('questionanswer')
        self.assertEqual(resolve(url).func,questionanswer)




class TestViews(TestCase):
    def setUp(self):
        self.client=Client()

    def test_questionanswer_GET(self):
        response=self.client.get(reverse('questionanswer'))
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'student/qa.html')