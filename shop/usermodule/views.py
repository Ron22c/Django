from django.shortcuts import render
from usermodule import forms

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    indexObj = {
        'welcome':'Welcome to the book shop'
    }
    return render(request,'usermodule/index.html',context=indexObj)


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse(index))


def signup(request):
    registered = False
    if request.method == "POST":
        user_form = forms.UserForm(data = request.POST)
        profile_form = forms.UserInformationForm(data = request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit = False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = forms.UserForm()
        profile_form = forms.UserInformationForm()

    return render(request, "usermodule/signup.html", {
        'user_form' : user_form,
        'profile_form' : profile_form,
        'registered' : registered
    })


def user_login(request):
    if request.method  == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username = username, password = password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse(index))
            else:
                return HttpResponse('Your profile is not activated')
        else:
            print('Failed to login with username {} and password {}'.format(username, password))
            return HttpResponse('Invalid Credentials')
    else:
        return render(request, 'usermodule/login.html', {})
