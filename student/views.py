from django.shortcuts import render
from rest_framework import viewsets

from Quizapp.models import Question, Exam
from .serializers import QuestionSerialzer, ExamSerializer

class QuestionViewset(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerialzer


class ExamViewset(viewsets.ModelViewSet):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer

class ExamQuestionViewset(viewsets.ModelViewSet):
    serializer_class = QuestionSerialzer
    queryset = Question.objects.filter(exam_id = 1)
    def get_queryset(self):
        return Question.objects.filter(exam_id=self.kwargs.get('pk'))
