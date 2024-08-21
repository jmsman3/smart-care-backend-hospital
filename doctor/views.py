from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.
from .models import Specialization,Designation,Doctor,AvailableTime,Review
from .serializers import SpecializationSerializers,DoctorSerializers ,DesignationtionSerializers,ReviewTimeSerializers,AvailableTimeSerializers
from rest_framework.permissions import IsAuthenticated ,IsAuthenticatedOrReadOnly
#pagination
from rest_framework import pagination , filters
# from rest_framework.pagination import PageNumberPagination

class SpecializationSpecificDoctor(filters.BaseFilterBackend):
    def filter_queryset(self, request, query_set, view):
        doctor_id = request.query_params.get("doctor_id")
        if doctor_id:
            return query_set.filter(doctor = doctor_id)
        return query_set
    
class SpecializationViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Specialization.objects.all() 
    serializer_class = SpecializationSerializers
    filter_backends = [SpecializationSpecificDoctor]


class DesignationSpecificDoctor(filters.BaseFilterBackend):
    def filter_queryset(self, request, query_set, view):
        doctor_id = request.query_params.get("doctor_id")
        if doctor_id:
            return query_set.filter(doctor = doctor_id)
        return query_set

class DesignationViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Designation.objects.all()
    serializer_class = DesignationtionSerializers
    filter_backends = [DesignationSpecificDoctor]

class AvailableTimeForSpecificDoctor(filters.BaseFilterBackend):
    def filter_queryset(self, request, query_set, view):
        doctor_id = request.query_params.get("doctor_id")
        if doctor_id:
            return query_set.filter(doctor = doctor_id)
        return query_set


class AvailableTimeViewset(viewsets.ModelViewSet):
    queryset = AvailableTime.objects.all()
    serializer_class = AvailableTimeSerializers
    filter_backends = [AvailableTimeForSpecificDoctor]

class DoctorPagination(pagination.PageNumberPagination):
    page_size=1 #items per page
    page_size_query_param = page_size
    max_page_size = 100


class DoctorViewset(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializers
    pagination_class = DoctorPagination

    
    def get_queryset(self):
        queryset = super().get_queryset() # 8 number line k as a parent aikhaen  e neye aslam 

        print(self.request.query_params)
        doctor_id = self.request.query_params.get("doctor_id")
        if doctor_id:
            queryset = queryset.filter(id = doctor_id)
        return queryset


class ReviewSpecificDoctor(filters.BaseFilterBackend):
    def filter_queryset(self, request, query_set, view):
        doctor_id = request.query_params.get("doctor_id")
        if doctor_id:
            return query_set.filter(doctor = doctor_id)
        return query_set



class ReviewViewset(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewTimeSerializers
    filter_backends = [ReviewSpecificDoctor]

    

