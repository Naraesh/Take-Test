from django.urls import path,include
from . import views
from rest_framework import routers

router=routers.DefaultRouter()
router.register('question',views.QuestionViewset)
router.register('exam',views.ExamViewset)

urlpatterns=[
    path('',views.index,name='index'),
    path('create/',views.create_user,name="create_user"),
    path('login/',views.log_in,name="log_in"),
    path('logout/',views.log_out,name="log_out"),
    path('examname/',views.add_exam,name="add_exam"),
    path('api',include(router.urls)),
    path('question/',views.add_question,name="add_question"),

]
