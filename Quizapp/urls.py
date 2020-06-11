from django.urls import path
from  .import views

urlpatterns = [
    path('',views.index),
    path('register/',views.register,name='register'),
    path('candidate/',views.candidate,name='student'),
    path('exadmin/',views.exadmin,name='uadmin'),
    path('reg/',views.canreg,name='reg'),
    path('login/',views.log,name='login'),
    path('logout/',views.signout,name='logout'),
    
]