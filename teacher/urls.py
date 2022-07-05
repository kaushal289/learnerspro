from django.urls import path
from teacher import views 

urlpatterns = [
    path('teacherregister',views.register, name="teacherregister"),
    path('teacherdashboard',views.teacherdashboard,name="teacherdashboard"),
    path('addsubjectpage', views.addsubjectpage, name='addsubjectpage'),
    path('teacherprofile/<int:s_id>',views.teacherprofile,name='teacherprofile'),
    path('profileupdateteacher/<int:s_id>',views.profileupdateteacher,name="profileupdateteacher"),
    path('logout',views.logout,name='logout'),
    path('email',views.email, name = "email"),
    path('reset',views.reset, name = "reset"),
    path('allcourse',views.allcourse, name = "allcourse"),
    path('editcourse/<int:c_id>',views.editcourse, name = "editcourse"),
    path('editquestion/<int:q_id>',views.editquestion, name = "editquestion"),
    path('updatequestion/<int:q_id>',views.updatequestion, name = "updatequestion"),
    path('courseupdate/<int:c_id>',views.courseupdate, name = "courseupdate"),
    path('deletecourse/<int:c_id>',views.deletecourse, name = "deletecourse"),
    path('questionview',views.questionview, name="questionview"),
    path('questiondelete/<int:q_id>',views.questiondelete, name = "questiondelete"),
]
