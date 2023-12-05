from django.shortcuts import render

# Create your views here.
from app.models import *

from app.serializers import *

from rest_framework.viewsets import ViewSet

from rest_framework.response import Response

class ProductData(ViewSet):
    def list(self,request):
        POD=Product.objects.all()
        JPD=ProductModelSerializer(POD,many=True)
        
        return Response(JPD.data)
    
    def retrieve(self,request,pk):
        POD=Product.objects.get(Pid=pk)
        JPD=ProductModelSerializer(POD)
        return Response(JPD.data)
    
    def create(self,request):
        JD=request.data
        PD=ProductModelSerializer(data=JD)

        if PD.is_valid():
            PD.save()

            return Response({'message':'Data is created'})

        else:
            return Response({'message':'Data is not created'})

    def update(self,request,pk):
        JD=request.data
        JPO=Product.objects.get(Pid=pk)
        PD=ProductModelSerializer(JPO,data=JD)

        if PD.is_valid():
            PD.save()

            return Response({'message':'Data is updated'})

        else:
            return Response({'message':'Data is not updated'})
        
    def partial_update(self,request,pk):
        JD=request.data
        JPO=Product.objects.get(Pid=pk)
        PD=ProductModelSerializer(JPO,data=JD,partial=True)

        if PD.is_valid():
            PD.save()

            return Response({'message':'Data is updated'})

        else:
            return Response({'message':'Data is not updated'})
        

    def destroy(self,request,pk):
        JD=request.data
        JOD=Product.objects.get(Pid=pk)
        PD=ProductModelSerializer(JOD,data=JD)
        JOD.delete()

        return Response({'message':'Data is deleted succesfully'})

