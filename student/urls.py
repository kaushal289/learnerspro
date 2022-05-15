from django.urls import path
from student import views 

urlpatterns = [
    path('',views.studentdashboard,name="studentdashboard"),
    path('studentregister',views.register, name="studentregister"),
    path('studentlogin',views.login, name="studentlogin"), 
]