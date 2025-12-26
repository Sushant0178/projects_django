from rest_framework import serializers
from students.models import student
from employee.models import Employee
from blog.models import Blogg , Comment
from .validators import adult_age


class studentSerializer(serializers.ModelSerializer):
    age = serializers.IntegerField(validators=[adult_age])
    class Meta:
        model = student 
        fields = '__all__'

class employeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'



class commentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

        
class bloggSerializer(serializers.ModelSerializer):  
    comments = commentSerializer(many=True, read_only=True)
    def get_comments(self, obj):
        comments = obj.comments.all()
        return commentSerializer(comments, many=True ).data
        
    class Meta:
        model = Blogg
        fields = '__all__'


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

