from rest_framework import serializers
from students.models import student
from employee.models import Employee
from blog.models import Blogg


class studentSerializer(serializers.ModelSerializer):
    class Meta:
        model = student 
        fields = '__all__'

class employeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

class bloggSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blogg
        fields = '__all__'