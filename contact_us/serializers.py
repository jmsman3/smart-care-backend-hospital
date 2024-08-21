from rest_framework import serializers
from .models import ContactUS

class ContactUsSerializers(serializers.ModelSerializer):
    class Meta:
        model = ContactUS
        fields = '__all__'