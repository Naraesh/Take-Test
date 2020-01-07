from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Exam,Question
from rest_framework import serializers,viewsets
from django.contrib.auth import authenticate, login, logout
from .serializer import QuestionSerialzer, ExamSerializer


# Create your views here.
def index(request):
    return render(request,'index.html')
def exam(request):
    context=Exam.objects.all()
    return render(request,'exam.html',{'context':context})
def taketest(request):
    cot=Exam.objects.all()
    return render(request,'taketest.html',{'cot':cot})
def edit(request, id):
    con=Exam.objects.get(id=id)
    return render(request,'addquestion.html',{'con':con})
def writeexam(request,id):
    con=Question.objects.filter(exam_id=id)
    return render(request,'writeexam.html',{'con':con})

def create_user(request):
    if request.method == 'POST':
        name =  request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = User.objects.create_user(username=name,email=email,password=password)
    return render(request,"index.html")
def log_in(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password  = request.POST.get("password")
        user = authenticate(username=username,password=password)
        if user is not None:
            if user.is_active:
                if username=='admin':
                    login(request,user)
                    return redirect('xam')
                else:
                    login(request,user)
                    return redirect('taketest')
        else:   
            return redirect('/')
def log_out(request):
    logout(request)
    return render(request,"index.html")

@login_required()
def add_exam(request):
    if request.method == 'POST':
        exam_name = request.POST.get("exam_name")
        user = request.POST.get("user")
        exam = Exam()
        exam.name = exam_name
        exam.user = User.objects.get(pk=user)
        exam.save()      
        return redirect('xam')
@login_required()
def add_question(request,id):
    if request.method == "POST":
        question  = request.POST.get("question")
        option1 = request.POST.get("option1")
        option2 = request.POST.get("option2")
        option3 = request.POST.get("option3")
        option4 = request.POST.get("option4")
        answer = request.POST.get("answer")
        exam = request.POST.get("exam")
        q = Question()
        q.question = question
        q.option1 = option1
        q.option2 = option2
        q.option3 = option3
        q.option4 = option4
        q.answer = answer
        q.exam = Exam.objects.get(id=int(exam))
        q.save()
        return redirect('xam')
 
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


