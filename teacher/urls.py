from django.urls import path
from teacher import views 

urlpatterns = [
    path('teacherregister',views.register, name="teacherregister"),
    path('teacherdashboard', views.teacherdashboard, name="teacherdashboard"),
    path('teachersubject', views.teachersubject, name="teachersubject"),
    path('addsubject/', views.addsubject, name='addsubject'),
    path('updatesubject/<int:pk>/', views.updatesubject, name='updatesubject'),
    path('deletesubject/<int:pk>/', views.deletesubject, name='deletesubject'),
    
]

