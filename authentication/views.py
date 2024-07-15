from django.http import HttpResponseBadRequest, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from  django.views.decorators.cache import cache_control 
from  django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from datetime import datetime, timedelta
from datetime import date
from django.core.paginator import Paginator
from django.urls import reverse
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.sessions.models import Session
from django.utils import timezone


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def Login(request):
    if request.user == None or request.user =="" or request.user.username == "":
        return render(request, "authentication/login.html")
    else:
        return HttpResponseRedirect(reverse('login'))
    
    
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def login_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = username, password = password)
        if user != None:
            login(request, user)
            messages.success(request, "Connexion reussie !")
            return redirect('home')
        else:
            messages.error(request, "Veuillez réssayer et verifier vos informations de connexion: nom utilisateur et mot de passe.")
            return HttpResponseRedirect(reverse('login'))

@login_required
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def logout_user(request):
    #deconnection du user avec la methode logout 
    logout(request)
    return redirect('/')
