from django.shortcuts import render
from .models import Destination
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import destinationSerializer

def index(request):
    dest1 = Destination()
    dest1.name = 'Mumbai'
    return render(request,"index.html",{'dest1':dest1})

class destiantionList(APIView):
    def get(self,request):
        dest = Destination.objects.all()
        serializer = destinationSerializer(dest,many=True)
        return Response(serializer.data)

    def post(self):
        pass
