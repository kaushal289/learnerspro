from django.urls import path
from teacher import views 

urlpatterns = [
    path('teacherregister',views.register, name="teacherregister"),
    path('teacherdashboard',views.teacherdashboard,name="teacherdashboard"),
    path('teachersubject', views.teachersubject, name="teachersubject"),
    path('addsubject/', views.addsubject, name='addsubject'),
    path('logout',views.logout,name='logout'),
<<<<<<< HEAD
    path('email',views.email, name = "email"),
    path('reset',views.reset, name = "reset"),
    path('allcourse',views.allcourse, name = "allcourse"),
    path('editcourse/<int:c_id>',views.editcourse, name = "editcourse"),
    path('courseupdate/<int:c_id>',views.courseupdate, name = "courseupdate"),
    path('deletecourse/<int:c_id>',views.deletecourse, name = "deletecourse"),
=======
>>>>>>> 25e845b2753558764247791987615d397bec9c40
]
