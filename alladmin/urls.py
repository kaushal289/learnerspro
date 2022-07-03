from django.urls import path
from alladmin import views 

urlpatterns = [
    path('admindash',views.admindash, name="admindash"),
    path('addadmin',views.addadmin, name="addadmin"),
    path('updatepassword/<int:s_id>',views.updatepassword, name ="updatepassword"),
    path('ticketview',views.ticketview, name="ticketview"),
    path('ticketdelete/<int:t_id>',views.ticketdelete, name = "ticketdelete"),
    path('addteacher',views.addteacher, name = "addteacher"),
    path('teacherview',views.teacherview, name="teacherview"),
    path('studentview',views.studentview, name="studentview"),
    path('adminupdate/<int:s_id>',views.adminupdate, name = "adminupdate"),
    path('teacherdelete/<int:td_id>',views.teacherdelete, name = "teacherdelete"),
    path('studentdelete/<int:td_id>',views.studentdelete, name = "studentdelete"),
]



