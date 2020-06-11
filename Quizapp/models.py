from django.contrib.auth.models import User
from django.db import models

class Exam(models.Model):
    name = models.CharField(max_length=100,default="")
    def __str__(self):
        return self.name

class Question(models.Model):
    question = models.TextField(max_length=200,default="")
    option1 = models.CharField(max_length=50,default="")
    option2 = models.CharField(max_length=50, default="")
    option3 = models.CharField(max_length=50, default="")
    option4 = models.CharField(max_length=50, default="")
    answer = models.CharField(max_length=50, default="")
    exam = models.ForeignKey(Exam,on_delete=models.CASCADE)