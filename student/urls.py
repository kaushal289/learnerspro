from django.urls import path
from student import views 

urlpatterns = [
    path('',views.studentdashboard,name="studentdashboard"),
    path('studentregister',views.register, name="studentregister"),
    path('studentlogin',views.login, name="studentlogin"), 
    path('userprofile',views.userprofile, name='userprofile'),
    path('student_update/<int:p_id>', views.update,name="student_update"),
]
