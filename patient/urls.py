from rest_framework.routers import DefaultRouter
from django.urls import path ,include
from .import views
router = DefaultRouter()

router.register('list', views.PatientViewset)
urlpatterns = [
    path('', include(router.urls)),
    path('register/', views.RegistrationApiView.as_view(),name='register'),
    path('login/', views.UserLoginApiview.as_view(),name='login'),
    path('logout/', views.UserLogoutView.as_view(),name='logout'),
    path('active/<uid64>/<token>', views.active,name='active'),
]
 
