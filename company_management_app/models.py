from django.db import models
from common_app.models import CommonModel
from django.conf import settings

# Create your models here.
class Company(CommonModel):
    company_id = models.AutoField(primary_key=True)
    shopkeeper = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    company_name = models.CharField(max_length=510, null=True, blank=True)
    company_address = models.TextField(null=True, blank=True)
    company_logo = models.ImageField(upload_to='uploads/images/company_logos', null=True, blank=True)
    company_banner = models.ImageField(upload_to='uploads/images/company_banners', null=True, blank=True)
    company_description = models.TextField(blank=True,null=True)
    gst_number = models.CharField(max_length=15, null=True, blank=True)
    business_email = models.EmailField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.company_name
