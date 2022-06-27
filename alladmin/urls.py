from django.urls import path
from alladmin import views 

urlpatterns = [
    path('admindash',views.admindash, name="admindash"),
    path('ticketview',views.ticketview, name="ticketview"),
    path('ticketdelete/<int:t_id>',views.ticketdelete, name = "ticketdelete"),
]

