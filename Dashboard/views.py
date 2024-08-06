from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from BusnesApp.models import BeginPageContent, ProjectCard, Illustrations, DevelopmentApproach

def index(request):

    begin_page_content = BeginPageContent.objects.first()
    project_card = ProjectCard.objects.all()
    illustrations = Illustrations.objects.first()
    development_approach = DevelopmentApproach.objects.first()

    context = {}
    context['begin_page_content'] = begin_page_content
    context['project_cards'] = project_card
    context['illustrations'] = illustrations
    context['development_approach'] = development_approach

    return render(request, 'dash/index.html', context)

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username', None)
        email = request.POST.get('email', None)
        password = request.POST.get('password', None)
        confirm_password = request.POST.get('confirm_password', None)

        if User.objects.filter(username=username).exists():
            text = "This username is already taken"
            return render(request, 'dash/error.html', {'message': text})

        if password != confirm_password:
            text = "Passwords do not match"
            return render(request, 'dash/error.html', {'message': text})

        User.objects.create_user(
            username=username,
            password=password,
            email=email
        )
        return redirect('index')

    return render(request, 'dash/register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('index')
    return render(request, 'dash/login.html')

def log_out(request):
    logout(request)
    return redirect('index')