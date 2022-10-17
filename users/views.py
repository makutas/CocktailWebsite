from django.contrib.auth import login
from django.shortcuts import render, redirect

from .forms import *


def register_new_user(request):
    if request.method == 'POST':
        form = CreateUserForm(data=request.POST)
        user_profile_form = UserProfileForm(data=request.POST)

        if form.is_valid() and user_profile_form.is_valid():
            user = form.save()
            user_profile = user_profile_form.save(commit=False)
            user_profile.user = user
            new_user = user_profile_form.save()
            login(request, new_user)
            return redirect('/')
    else:
        form = CreateUserForm()
        user_profile_form = UserProfileForm()

    context = {
        'form': form,
        'user_profile_form': user_profile_form
    }

    return render(request, "registration/register.html", context)
