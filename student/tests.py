from django.test import SimpleTestCase,TestCase,Client
from django.urls import reverse,resolve
from student.views import *
# Create your tests here.

class TestUrls(SimpleTestCase):
    def test_case_question_url(self):
        url=reverse('question')
        self.assertEqual(resolve(url).func,question)
    def test_case_studentsubject_url(self):
        url=reverse('studentsubject')
        self.assertEqual(resolve(url).func,question)




class TestViews(TestCase):
    def setUp(self):
        self.client=Client()

    def test_question_GET(self):
        response=self.client.get(reverse('question'))
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'student/question.html')

    def test_studentsubject_GET(self):
        response=self.client.get(reverse('studentsubject'))
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'student/studentsubject.html')
