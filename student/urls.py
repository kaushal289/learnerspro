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
    
]
>>>>>>> 0dbb72373c7cb5b26df76361178695293155c0bf
