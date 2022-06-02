from django.urls import path
from teacher import views 

urlpatterns = [
    path('teacherregister',views.register, name="teacherregister"),
<<<<<<< HEAD
    path('teacherdashboard',views.teacherdashboard,name="teacherdashboard"),
]
=======
    path('teacherdashboard', views.teacherdashboard, name="teacherdashboard"),
    path('teachersubject', views.teachersubject, name="teachersubject"),
    path('addsubject/', views.addsubject, name='addsubject'),
    path('updatesubject/<int:pk>/', views.updatesubject, name='updatesubject'),
    path('deletesubject/<int:pk>/', views.deletesubject, name='deletesubject'),
    
]

>>>>>>> 743cd069bdf10af63f6d89ae0d24ae8322a15528
