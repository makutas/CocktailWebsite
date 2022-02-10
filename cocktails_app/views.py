from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .models import *


@login_required(login_url='users:login')
def index(request):
    return render(request, "index.html")
