from django.urls import path
from alladmin import views 

urlpatterns = [
    path('admindash',views.admindash, name="admindash"),
    path('updatepassword',views.updatepassword, name = "updatepassword"),
<<<<<<< HEAD
    path('updatepasswordfield/<int:a_id>',views.updatepasswordfield, name = "updatepasswordfield"),
=======
>>>>>>> 384ec8fd38352e2c4150146c41f2c795daef07fc
    path('ticketview',views.ticketview, name="ticketview"),
    path('ticketdelete/<int:t_id>',views.ticketdelete, name = "ticketdelete"),
    path('addteacher',views.addteacher, name = "addteacher"),
    path('teacherview',views.teacherview, name="teacherview"),
    path('teacherdelete/<int:td_id>',views.teacherdelete, name = "teacherdeletedelete"),
]



