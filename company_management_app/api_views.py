from rest_framework import status
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from company_management_app.models import Company
from rest_framework.mixins import CreateModelMixin
from company_management_app.serializers import *
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404

# Create your views here.
class CompanyProfile(CreateModelMixin, RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CompanySerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['user'] = self.request.user
        return context

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get_object(self):
        obj = Company.objects.filter(shopkeeper=self.request.user).first()
        return obj
