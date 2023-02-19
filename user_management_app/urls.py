from django.urls import path, include
from user_management_app import api_views, views
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('login/', api_views.Login.as_view()),
    path('', views.UserLoginForm, name='sign-in'),

    path('register/', api_views.Register.as_view()),
    path('sign-up/', views.UserRegisterForm, name='sign-up'),

    path('logout/', views.UserLogout, name='logout'),
    
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('user/', api_views.RetrieveUpdateDestroyUser.as_view()),

    path('update-profile/', views.UpdateUserProfie, name='update-profile'),
    path('delete-profile/', views.DeleteUserProfile, name='delete-profile'),
]