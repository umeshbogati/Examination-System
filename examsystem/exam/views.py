from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Exam, Question
from django.contrib.auth.models import User
from django.contrib import messages

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
    score = 0
    total = questions.count()
    
    if request.method == "POST":
        for q in questions:
            selected = request.POST.get(str(q.id))
            if selected == q.correct_answer:
                score += 1
        return render(request, 'result.html', {
            'score': score,
            'total': total
            
        })
    return render(request, 'take_exam.html', {'questions': questions})

from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, redirect

def student_register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
        else:
            User.objects.create_user(username=username, password=password)
            messages.success(request, "Account created successfully")
            return redirect('login')

    return render(request, 'exam/register.html')
