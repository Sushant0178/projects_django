from django.shortcuts import render
from django.http import HttpResponse
from .forms import EmployeeForm, UserForm
from django.shortcuts import redirect
from .models import Employee
from django.contrib.auth import authenticate , login , logout
from django.contrib import messages
from django.db.models import Sum
from django.contrib.auth.models import User

# from django.contrib.auth.models import User

def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful. You can now log in.")
            return redirect('home')
    else:
        form = UserForm()
    
    return render(request, 'employees/register.html', {'form': form})


def home(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            messages.success(request, "Logged in successfully.")
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid username or password.")
            return redirect('home')
    
    return render(request, 'employees/index.html')



def logout_user(request):
    logout(request)
    messages.success(request, "Logged out successfully.")
    return redirect('home')




def allemployees(request):
        employees = Employee.objects.all()

        return render(request, 'employees/all_employees.html',{'employees':employees})
        # return render(request, 'base.html')
    


def singleemployee(request, empid): 

    if request.user.is_authenticated:
        employee = Employee.objects.get(id=empid)
    else:
        return redirect('home')
    
    return render(request, 'employees/single_employee.html' , {'employee': employee})


def addemployee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("all_employees")
    else:
        form = EmployeeForm()
        # return HttpResponse("Employee added successfully!")
        

    return render(request, 'employees/add_employee.html', {'form': form})


def deleteemployee(request , empid):
   if request.user.is_authenticated:
        employee = Employee.objects.get(id=empid)
        employee.delete()
        return redirect('all_employees')
   else:
        return redirect('home')
    

def editemployee(request , empid):
    if request.user.is_authenticated:
        employee = Employee.objects.get(id=empid)
        form = EmployeeForm(request.POST , instance = employee)
        if form.is_valid():
            form.save()
            messages.success(request , "record has been updated")
            return redirect('all_employees')
        else:
            form = EmployeeForm(instance=employee)
        return render(request , 'employees/edit_employee.html', {'form':form})

        













def dashboard(request):
    total_employees = Employee.objects.count()
    total_salary = Employee.objects.aggregate(total=Sum('salary'))['total'] or 0
    active_users = User.objects.filter(is_active=True).count()
    total_positions = Employee.objects.values('position').distinct().count()

    context = {
        'employees_count': total_employees,
        'total_salary': total_salary,
        'active_users': active_users,
        'position_count': total_positions,
    }

    return render(request, 'employees/dashboard.html', context)

