from django.test import SimpleTestCase,TestCase,Client
from django.urls import reverse,resolve
from student.views import *
# Create your tests here.

class TestUrls(SimpleTestCase):
    def test_case_index_url(self):
        url=reverse('studentdashboard')
        self.assertEqual(resolve(url).func,studentdashboard)

    def test_case_register_url(self):
        url=reverse('studentregister')
        self.assertEqual(resolve(url).func,register)

    def test_case_login_url(self):
        url=reverse('studentlogin')
        self.assertEqual(resolve(url).func,login)



class TestViews(TestCase):
    def setUp(self):
        self.client=Client()

    def test_register_GET(self):
        response=self.client.get(reverse('studentdashboard'))
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'student/landingpage.html')

    def test_login_GET(self):
        response=self.client.get(reverse('studentlogin'))
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'reglogin/login.html')
    
    def test_dashboard_GET(self):
        response=self.client.get(reverse('studentregister'))
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'reglogin/registration.html')
