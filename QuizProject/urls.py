from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('Quizapp.urls')),
    path('adminpart/',include('adminpart.urls')),
    path('student/',include('student.urls')),
]
