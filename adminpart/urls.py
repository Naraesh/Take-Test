from django.urls import path
from . import views

urlpatterns = [
    path('catergoryadd/', views.catergoryadd,name='catergoryadd'),
    path('userverify/',views.userverify,name='userverify'),
    path('approve/<int:id>',views.approve,name='approve'),
    path('viewquestion/<int:id>',views.viewquestion,name='viewquestion'),
    path('addquestion/',views.addquestion,name='addquestion'),
]
