from django.urls import path
from teacher import views 

urlpatterns = [
    path('teacherregister',views.register, name="teacherregister"),
    path('teacherdashboard',views.teacherdashboard,name="teacherdashboard"),
]
