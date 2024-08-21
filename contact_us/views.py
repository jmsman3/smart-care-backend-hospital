from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.
from .models import ContactUS
from .serializers import ContactUsSerializers

class ContactUsViewset(viewsets.ModelViewSet):
    queryset = ContactUS.objects.all()
    serializer_class = ContactUsSerializers
    
