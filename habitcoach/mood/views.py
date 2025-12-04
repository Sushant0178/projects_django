from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.



def mood_home(request):
    return HttpResponse("Welcome to the Mood Tracker Home Page")

    # return render(request, 'mood/mood_home.html')