from django.shortcuts import render
from django.http import HttpResponse    
# Create your views here.
def tasks_home(request):
    return HttpResponse("Welcome to the Tasks Home Page")


    # return render(request, 'notifications/notifications_home.html')