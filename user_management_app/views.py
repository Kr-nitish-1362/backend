from user_management_app.models import UserAccount
from user_management_app.serializers import *
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import generics, status
from rest_framework.response import Response
from django.contrib.auth import authenticate, get_user_model
from django.shortcuts import get_object_or_404
from django.utils import timezone

# Create your views here.
class Register(generics.CreateAPIView):
    serializer_class = RegisterUserSerializer
    queryset = UserAccount.objects.all()

class Login(generics.GenericAPIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        username = None
        
        if email:
            user_object = UserAccount.objects.filter(email=email).first()
            if user_object is not None:
                username = user_object.username
        else:
            return Response(
                {'error': 'Some parameter is missing!'}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
        user_obj = authenticate(username=username, password=password)
        if user_obj is not None:
            user_obj.save()
            result = {}
            # Generate a JWT Token for the admin
            refresh = RefreshToken.for_user(user_obj)
            result["access_token"] = str(refresh.access_token)
            result["refresh_token"] = str(refresh)

            return Response(result, status=status.HTTP_200_OK)
        else:
            return Response(
                    {'error': 'username or password is incorrect!'}, 
                    status=status.HTTP_400_BAD_REQUEST
                )

class RetrieveUpdateDestroyUser(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = RetrieveUpdateDestroyUserSerialiser
    queryset = UserAccount.objects.all()

    def get_object(self):
        obj = get_object_or_404(get_user_model(), pk=self.request.user.user_id)
        return obj

