from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.
from .models import Appointment
from .serializers import AppointmentSerializers

class AppointmentViewset(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializers

    def get_queryset(self):
        queryset = super().get_queryset() # 8 number line k as a parent aikhaen  e neye aslam 
        print(self.request.query_params)
        patient_id = self.request.query_params.get("patient_id")
        if patient_id:
            queryset = queryset.filter(patient_id = patient_id)
        return queryset

