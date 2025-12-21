from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter



router = DefaultRouter()
router.register('employees', views.EmployeeViewset, basename='employees') 
router.register('blogs', views.BloggViewset, basename='blogs')
# u dont need to add basename='employees' if the viewset has a queryset attribute defined, 
# as the router can automatically determine the base name from the model associated with the queryset.

urlpatterns = [
    path('students/', views.StudentsViews),
    path('students/<int:pk>/', views.StudentDetailView),
    # path('employees/',views.Employees.as_view()),
    # path('employees/<int:pk>/', views.EmployeesDetail.as_view()),
    path('', include(router.urls)),
]

    


