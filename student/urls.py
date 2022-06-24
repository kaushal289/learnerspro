from django.urls import path
from student import views 


urlpatterns = [
    path('',views.studentdashboard,name="studentdashboard"),
    path('studentregister',views.register, name="studentregister"),
    path('studentlogin',views.studentlogin,name="studentlogin"),
    path('logout',views.logout,name='logout'),
    path('studentprofile/<int:s_id>',views.studentprofile,name='studentprofile'),
    path('profileupdate/<int:s_id>',views.profileupdate,name="profileupdate"),
    path('class6', views.class6, name='class6'),
    path('class7', views.class7, name='class7'),
    path('class6science', views.class6science, name='class6science'),
    path('class6english', views.class6english, name='class6english'),
    path('class7math', views.class7math, name='class7math'),
    path('questionanswer', views.questionanswer, name='questionanswer'),
    path('question', views.question, name='question'),
    path('ticket',views.ticket, name='ticket'),
]