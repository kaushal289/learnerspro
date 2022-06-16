from django.urls import path
from teacher import views 

urlpatterns = [
    path('teacherregister',views.register, name="teacherregister"),
    path('teacherdashboard',views.teacherdashboard,name="teacherdashboard"),
    path('teachersubject', views.teachersubject, name="teachersubject"),
    path('addsubject/', views.addsubject, name='addsubject'),
    path('teacherprofile/<int:s_id>',views.teacherprofile,name="teacherprofile"),
    path('logout',views.logout,name='logout'),
]
