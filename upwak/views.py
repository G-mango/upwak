# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, render_to_response, redirect

from django.shortcuts import render

# Create your views here.


def wak_login(request):
    return render_to_response('login.html')


def wak_signup(request):
    return render_to_response('signup.html')


def wak_dashboard(request):
    return render_to_response('index.html')


