from django.urls import path, include
from user_management_app import views
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('register/', views.Register.as_view()),
    path('login/', views.Login.as_view()),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('user/', views.RetrieveUpdateDestroyUser.as_view()),
]