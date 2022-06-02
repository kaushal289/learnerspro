from django.urls import path
from student import views 

urlpatterns = [
    path('',views.studentdashboard,name="studentdashboard"),
    path('studentregister',views.register, name="studentregister"),
    path('studentlogin',views.studentlogin,name="studentlogin"),
    path('logout',views.logout,name='logout'),
<<<<<<< HEAD
    path('studentsubject', views.studentsubject, name="studentsubject"),
]
=======
<<<<<<< HEAD
    path('profile',views.profile,name="profile"),
]
=======
<<<<<<< HEAD
    path('studentsubject', views.studentsubject, name="studentsubject"),
]
=======
]

>>>>>>> 91b04a5412e80f3a98e0d45fe4c4e84be1774a7d
>>>>>>> 885fba9f041c70726c7f4f0dfe0ec7378587f4df
>>>>>>> d9ac5b5e5e0d6e03a95d56250fb727b24845093e
