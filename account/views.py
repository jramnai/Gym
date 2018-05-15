# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from forms import SignUpForm
from django.contrib.auth.decorators import login_required

# Create your views here


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.full_name = form.cleaned_data.get('full_name')
            user.profile.mobile = form.cleaned_data.get('mobile')

            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('gym:index')
    else:
        form = SignUpForm()
    return render(request, 'account/signup.html', {'form': form})


@login_required
def detail(request):
    return render(request, 'account/detail.html')
