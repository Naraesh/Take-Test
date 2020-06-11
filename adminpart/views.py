from django.shortcuts import render,redirect
from Quizapp.models import Exam,Question
from django.http import HttpResponse,JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

@login_required(login_url='/')
def catergoryadd(request):
    if request.method=='POST':
        exam=request.POST.get("msg")
        obj=Exam.objects.create(name=exam)
        cont={'id':obj.id,'name':obj.name}
        return JsonResponse({'data':cont})

@login_required(login_url='/')
def approve(request,id):
    user=User.objects.get(id=id)
    user.is_active=True
    user.save()
    return redirect('userverify')

@login_required(login_url='/')
def userverify(request):
    con=User.objects.all()
    return render(request,'userverify.html',{'context':con})

@login_required(login_url='/')
def addquestion(request):
    if request.method=='POST':
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

        # obj=Question.objects.get(question=question)
        # con={'id':obj.id,'question':obj.question,'option1':obj.option1,'option2':obj.option2,'option3':obj.option3,'option4':obj.option4,'answer':obj.answer}
        return HttpResponse('success')

@login_required(login_url='/')
def viewquestion(request,id):
    ans=Question.objects.filter(exam_id=id)
    return render(request,'viewquestion.html',{'con':ans})

