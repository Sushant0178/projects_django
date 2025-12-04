
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse

def home_view(request):
    return render(request, 'index.html')


