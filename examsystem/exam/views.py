from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Exam, Question


# Create your views here.
def student_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('exam_list')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')

def student_logout(request):
    logout(request)
    return redirect('login') 


@login_required
def exam_list(request):
    exams = Exam.objects.all()
    return render(request, 'exam_list.html', {'exams': exams})

@login_required
def take_exam(request, exam_id):
    questions = Question.objects.filter(exam_id=exam_id)
    return render(request, 'take_exam.html', {'questions': questions})