from django.urls import path
from student import views 


urlpatterns = [
    path('',views.studentdashboard,name="studentdashboard"),
    path('studentregister',views.register, name="studentregister"),
    path('studentlogin',views.studentlogin,name="studentlogin"),
    path('logout',views.logout,name='logout'),
    path('studentprofile/<int:s_id>',views.studentprofile,name='studentprofile'),
    path('profileupdate/<int:s_id>',views.profileupdate,name="profileupdate"),
]
