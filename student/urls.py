from django.urls import path
from student import views 

urlpatterns = [
    path('',views.studentdashboard,name="studentdashboard"),
    path('studentregister',views.register, name="studentregister"),
    path('studentlogin',views.studentlogin,name="studentlogin"),
    path('logout',views.logout,name='logout'),
<<<<<<< HEAD
    path('studentsubject', views.studentsubject, name="studentsubject"),
]
=======
]

>>>>>>> 91b04a5412e80f3a98e0d45fe4c4e84be1774a7d
