from django import forms
from .models import Employee
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserForm(UserCreationForm):
    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(attrs={
            'class': 'form-control form-control-lg w-100',
            'placeholder': 'example@email.com'
        })
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control form-control-lg w-100',
                'placeholder': 'Enter username'
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    
        self.fields['password1'].widget.attrs.update({
            'class': 'form-control form-control-lg w-100',
            'placeholder': 'Enter password'
        })

        self.fields['password2'].widget.attrs.update({
            'class': 'form-control form-control-lg w-100',
            'placeholder': 'Confirm password'
        })




class EmployeeForm(forms.ModelForm):
    
    hire_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}))


    class Meta:
        model = Employee
        fields = ['first_name', 'last_name', 'email', 'position', 'salary', 'hire_date', 'phone_number']

        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'position': 'Job Position',
            'salary': 'Salary',
            'hire_date': 'Hire Date',
        }

        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter first name'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter last name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'example@email.com'
            }),
            'phone_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter phone number'
            }),
            'position': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Job title'
            }),
            'salary': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Salary amount'
            }),
        }

    
