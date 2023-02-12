from django.urls import path, include
from company_management_app import views

urlpatterns = [
    path('company/', views.CompanyProfile.as_view()),
    
]