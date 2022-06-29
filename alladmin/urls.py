from django.urls import path
from alladmin import views 

urlpatterns = [
    path('admindash',views.admindash, name="admindash"),
<<<<<<< HEAD
    path('updatepassword',views.updatepassword, name = "updatepassword"),
    
=======
    path('ticketview',views.ticketview, name="ticketview"),
    path('ticketdelete/<int:t_id>',views.ticketdelete, name = "ticketdelete"),
    path('addteacher',views.addteacher, name = "addteacher"),
    path('teacherview',views.teacherview, name="teacherview"),
    path('teacherdelete/<int:td_id>',views.teacherdelete, name = "teacherdeletedelete"),
>>>>>>> 0a75ca3717b602bd05567c0daefc1309c0e09115
]



