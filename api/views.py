from django.shortcuts import render
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import permissions, status

# Create your views here.


class Home(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        
        return Response({
            'message': 'data received',
            'payload': request.data
            })