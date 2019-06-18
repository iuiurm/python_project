from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('boards:index')
    else:  # GET accounts/signup/
        form = UserCreationForm()
    context = {'form': form}
    return render(request, 'accounts/signup.html', context)


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        #  사용자 입력 유효성 검사
        if form.is_valid():
            #  로그인
            auth_login(request, form.get_user())
            return redirect('boards:index')
    else:  # GET /accounts/login/ -> html 페이지만 렌더링
        form = AuthenticationForm()
    context = {'form': form}
    return render(request, 'accounts/login.html', context)


def logout(request):
    #  로그아웃 로직
    auth_logout(request)
    return redirect('boards:index')
