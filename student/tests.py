from django.test import SimpleTestCase,TestCase,Client
from django.urls import reverse,resolve
from student.views import *
# Create your tests here.

class TestUrls(SimpleTestCase):
    def test_case_studentsubject_url(self):
        url=reverse('studentsubject')
        self.assertEqual(resolve(url).func,studentsubject)



class TestViews(TestCase):
    def setUp(self):
        self.client=Client()

    def test_studentsubject_GET(self):
        response=self.client.get(reverse('studentsubject'))
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'student/studentsubject.html')
        
