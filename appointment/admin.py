from django.contrib import admin
from .models import Appointment

#Email
from django.core.mail import EmailMultiAlternatives,send_mail
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from django.shortcuts import redirect
# Register your models here.
class AppointmentModelAdmin(admin.ModelAdmin):
    list_display = ['patient_name','doctor_name','appointment_types','appointment_status','symptom','time','cancel']

    def patient_name(self,obj):
        return obj.patient.user.first_name
    def doctor_name(self,obj):
        return obj.doctor.user.first_name
    

    def save_model(self,request,obj,form,change):
        obj.save()

        if obj.appointment_status =="Running" and obj.appointment_types == "Online":
            email_subject = "Your Online Appointment is Running"
            email_body = render_to_string('admin_Appointment_email.html', {'user' : obj.patient.user ,'doctor' :obj.doctor})
            
            email = EmailMultiAlternatives(email_subject , '', to=[obj.patient.user.email])
            email.attach_alternative(email_body, "text/html")
            email.send()
            

    
admin.site.register(Appointment ,AppointmentModelAdmin)
