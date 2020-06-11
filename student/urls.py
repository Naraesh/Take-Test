from django.urls import path,include
from . import views
from rest_framework import routers

from .views import ExamQuestionViewset,QuestionViewset, ExamViewset


router = routers.DefaultRouter()
router.register('question',QuestionViewset)
router.register('exam',ExamViewset)

urlpatterns = [
    path('api/',include(router.urls)),
    
]
