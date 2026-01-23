from django.urls import path
from . import views

urlpatterns = [
    path('', views.home , name='home'),
    # path('userlogin', views.login_user , name='userlogin'),
    path('register', views.register , name='register'),
    path('userlogout', views.logout_user , name='userlogout'),
    path('allemployees/', views.allemployees, name='all_employees'),
    path('singleemployee/<int:empid>/', views.singleemployee, name='single_employee'),
    path('addemployee/', views.addemployee, name='add_employee'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('deleteemployee/<int:empid>/', views.deleteemployee, name='delete_employee'),
    path('editemployee/<int:empid>/', views.editemployee, name='edit_employee'),


]