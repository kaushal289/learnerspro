from django.urls import path
from teacher import views 

urlpatterns = [
    path('teacherregister',views.register, name="teacherregister"),
    path('teacherdashboard',views.teacherdashboard,name="teacherdashboard"),
<<<<<<< HEAD
    path('teachersubject', views.teachersubject, name="teachersubject"),
    path('addsubject/', views.addsubject, name='addsubject'),
    path('logout',views.logout,name='logout'),
=======
>>>>>>> 91b04a5412e80f3a98e0d45fe4c4e84be1774a7d
]
