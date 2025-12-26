from django.shortcuts import render
from django.http import HttpResponse , JsonResponse
from employee.models import Employee
from students.models import student
from .serializers import studentSerializer , employeeSerializer
from rest_framework.response import Response
from rest_framework import status 
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import generics , mixins , viewsets
from rest_framework.generics import ListCreateAPIView
from rest_framework.viewsets import ModelViewSet
from blog.models import Blogg , Comment
from .serializers import bloggSerializer , commentSerializer , LoginSerializer
from .pagination import CostomPagination
from .filters import EmployeeFilter
from .filters import BloggFilter
from rest_framework.filters import SearchFilter , OrderingFilter
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated




# @api_view(['GET' , 'POST'])
# def StudentsViews(request):
#     if request.method  == 'GET': 
#         # get all the data from the student table 
#         students = student.objects.all()
#         serializer = studentSerializer(students , many = True)
#         return Response(serializer.data , status=status.HTTP_200_OK)
#     elif request.method == 'POST':
#         serializer = studentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response (serializer.data , status=status.HTTP_201_CREATED )
#         return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
    
class StudentsViews(generics.ListCreateAPIView):
    queryset = student.objects.all()
    serializer_class = studentSerializer


# @api_view(['GET', 'PUT' , 'DELETE', 'PATCH'])
# def StudentDetailView(request, pk):
#     try:  
#         students = student.objects.get(pk=pk)
#     except student.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
    
#     if request.method == 'GET':
#         serializer = studentSerializer(students)
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
#     elif request.method == 'PUT':
#         serializer = studentSerializer(students, data=request.data)
#         if serializer.is_valid():
#             serializer.save()

#             return Response(serializer.data, status=status.HTTP_200_OK)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     elif request.method == 'DELETE':
#         students.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    
#     elif request.method == 'PATCH':
#         serializer = studentSerializer(students, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StudentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = student.objects.all()
    serializer_class = studentSerializer




#---------------------------------class based views -----------------------------------------------------------------------------

# class Employees(APIView):
#     def get(self,request):
#         employees = Employee.objects.all()
#         serializer = employeeSerializer(employees, many=True)
#         return Response(serializer.data , status=status.HTTP_200_OK)
    
#     def post(self , request):
#         serializer= employeeSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data , status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class EmployeesDetail(APIView):
#     def get_object(self , pk):
#         try :
#             employee = Employee.objects.get(pk = pk)
#             return employee
#         except Employee.DoesNotExist:
#             raise Http404
        
#     def  get(self ,request, pk):
#         employe = self.get_object(pk)
#         serializer = employeeSerializer(employe)
#         return Response(serializer.data , status=status.HTTP_200_OK)
    
#     def delete(self , request , pk):
#         employe = self.get_object(pk)
#         employe.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    
#     def put(self , request , pk):
#         employe = self.get_object(pk)
#         serializer = employeeSerializer(employe , data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data , status=status.HTTP_200_OK)    
#         return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
    
#     def patch(self , request , pk):
#         employe = self.get_object(pk)
#         serializer = employeeSerializer(employe , data = request.data , partial = True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data , status=status.HTTP_200_OK)    
#         return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)


#--------------------------------------------------using mixins and generics -------------------------------------------------------

# class Employees(mixins.ListModelMixin,mixins.CreateModelMixin, generics.GenericAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = employeeSerializer

#     def get(self,request):
#         return self.list(request)
    
#     def post(self,request):
#         return self.create(request)
    


    
# class EmployeesDetail(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView,generics.CreateAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = employeeSerializer

#     def get(self,request,pk):
#         return self.retrieve(request , pk)
    
    
#     def put(self,request,pk):
#         return self.update(request , pk)
    
#     def delete(self,request,pk):
#         return self.destroy(request , pk)   
     
    
    

#--------------------------------------------------using generics only -------------------------------------------------------



'''
class Employees(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = employeeSerializer


    
class EmployeesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = employeeSerializer
    lookup_field = 'pk' 

'''




#--------------------------------------------------using viewsets -------------------------------------------------------

# class EmployeeViewset(viewsets.ViewSet):
#     def list(self, request):
#         queryset = Employee.objects.all()
#         serializer = employeeSerializer(queryset, many=True)
#         return Response(serializer.data)
    
#     # post method
#     def create(self, request):
#         serializer = employeeSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
        
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

#     # get method
#     def retrieve(self, request, pk=None):
#         employee = Employee.objects.get(pk=pk)
#         serializer = employeeSerializer(employee)
#         return Response(serializer.data)
    
#     # put method
#     def update(self, request, pk=None):
        
#         employee = Employee.objects.get(pk=pk)
#         serializer = employeeSerializer(employee, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
        
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     # delete method
#     def destroy(self, request, pk=None):   
#         employee = Employee.objects.get(pk=pk)
#         employee.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    


#--------------------------------------------------using ModelViewsets -------------------------------------------------------

class EmployeeViewset(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = employeeSerializer
    lookup_field = 'pk'
    pagination_class = CostomPagination   #<-------------------- costom pagination 
    # filterset_fields = ['emp_name' ]  #<-------------------- adding filter fields
    filterset_class = EmployeeFilter
    





#-------------------------------------------------- Blogg ModelViewsets -------------------------------------------------------
# class BloggViewset(ModelViewSet):
#     queryset = Blogg.objects.all()
#     serializer_class = bloggSerializer
#     lookup_field = 'pk'

class blogsView(generics.ListCreateAPIView):
    queryset = Blogg.objects.all()
    serializer_class = bloggSerializer
    filterset_class = BloggFilter
    filter_backends = [SearchFilter , OrderingFilter]
    search_fields = ['blogger_title' , 'text']
    ordering_fields = ['id' , 'blogger_name'] #<-------------------- ordering fields we can change the ordering based on these fields
    # lookup_field = 'pk'
    
class commentsView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()  
    serializer_class = commentSerializer

class blogdetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blogg.objects.all()
    serializer_class = bloggSerializer
    lookup_field = 'pk'
    

class commentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = commentSerializer
    lookup_field = 'pk'



class LoginApi(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        print(request.user)
        
        data = request.data
        serializer = LoginSerializer(data=data)
        if not serializer.is_valid():
            return Response({
            "status": False,
            "data": serializer.errors   
        })
        username = serializer.validated_data['username']
        password = serializer.validated_data['password']

        user_obj = authenticate(username=username, password=password) # authenticating user from the db

        if user_obj:
    
            Token_obj , _ = Token.objects.get_or_create(user=user_obj)
            print(Token_obj)
            return Response({
            "status": True,
            "data": {'token':str(Token_obj) },
        })



        return Response({
            "status": False,
            "data": {},
            "message": "Invalid username or password"
        })









    
