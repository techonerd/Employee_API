from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import employee as employeeModel
from .serializers import employeeSerializer

# Create your views here.
class employeelist(APIView):
    def get (self,request):
        employee1=employeeModel.objects.all()
        serializer=employeeSerializer(employee1, many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer= employeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
