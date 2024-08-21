from django.contrib import admin
from .models import Specialization,Designation,AvailableTime,Doctor,Review
# Register your models here.

class AdminSpecialization(admin.ModelAdmin):
    prepopulated_fields ={"slug": ("name",),}
admin.site.register(Specialization ,AdminSpecialization)

class AdminDesignation(admin.ModelAdmin):
    prepopulated_fields ={"slug": ("name",),}
admin.site.register(Designation , AdminDesignation)

admin.site.register(AvailableTime)

class DoctorModelAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name','fee','meet_link']

    def first_name(self,obj):
        return obj.user.first_name
    def last_name(self,obj):
        return obj.user.last_name

admin.site.register(Doctor ,DoctorModelAdmin)

class ReviewModelAdmin(admin.ModelAdmin):
    list_display = ['reviewer','doctor','created','rating']
admin.site.register(Review ,ReviewModelAdmin)
