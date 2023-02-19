from django.urls import path, include
from company_management_app import api_views, views

urlpatterns = [
    path('company/', api_views.CompanyProfile.as_view()),
    path('add-company/', views.CompanyForm, name='add-company'),
    path('update-company/', views.UpdateCompanyForm, name='update-company'),
    path('delete-company/', views.DeleteCompany, name='delete-company'),
]