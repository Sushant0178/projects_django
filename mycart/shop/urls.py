from django.conf import settings
from django.contrib import admin
from django.urls import path
from . import views


from .import views
from django.conf.urls.static import static
urlpatterns = [
    path('',views.index , name='in'),
    path('about/', views.about , name='AboutUs'),
    path('contact/', views.contact , name='ContactUs'),
    path('tracker/', views.tracker , name='TrakingStatus'),
    path('search/', views.search , name='Search'),
    path('productview/', views.prodView , name='PdrouctView'),
    path('cheakout/', views.cheakout , name='Cheakout'),





]


