from rest_framework import serializers
from .models import Specialization,Designation,AvailableTime,Doctor,Review

class SpecializationSerializers(serializers.ModelSerializer):
    class Meta:
        model = Specialization
        fields = '__all__'

class DesignationtionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Designation
        fields = '__all__'

class AvailableTimeSerializers(serializers.ModelSerializer):
    class Meta:
        model = AvailableTime
        fields = '__all__'
        
class DoctorSerializers(serializers.ModelSerializer):
    user = serializers.StringRelatedField(many=False)
    specialization = serializers.StringRelatedField(many=True)
    designation = serializers.StringRelatedField(many=True)
    available_time = serializers.StringRelatedField(many=True)
    class Meta:
        model = Doctor
        fields = '__all__'

class ReviewTimeSerializers(serializers.ModelSerializer):
    # reviewer = serializers.StringRelatedField(many=False)
    # doctor = serializers.StringRelatedField(many=False)
    class Meta:
        model = Review
        fields = '__all__'
