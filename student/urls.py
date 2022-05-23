from django.urls import path
from student import views 

urlpatterns = [
    path('',views.studentdashboard,name="studentdashboard"),
    path('studentregister',views.register, name="studentregister"),
    path('studentlogin',views.studentlogin,name="studentlogin"),
    path('logout',views.logout,name='logout'),
    path('userprofile',views.profile, name='profile'),
    path('updateprofile/<int:p_id>', views.updateprofile,name="updateprofile"),
]
