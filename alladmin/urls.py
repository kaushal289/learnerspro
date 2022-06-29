from django.urls import path
from alladmin import views 

urlpatterns = [
    path('admindash',views.admindash, name="admindash"),
    path('updatepassword',views.updatepassword, name = "updatepassword"),
    
]



