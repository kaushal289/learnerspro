from django.urls import path
from student import views 

urlpatterns = [
    path('',views.studentdashboard,name="studentdashboard"),
    path('studentregister',views.register, name="studentregister"),
    path('studentlogin',views.studentlogin,name="studentlogin"),
    path('logout',views.logout,name='logout'),
<<<<<<< HEAD
]

=======
    path('studentsubject', views.studentsubject, name="studentsubject"),
]
>>>>>>> 2dba6ee068f458507b4b0c0aac1e8ab81334b7e0
