from django.urls import path
from addcourse import views 

urlpatterns = [
    path('addcourse',views.addcourse, name="addcourse"),
]

