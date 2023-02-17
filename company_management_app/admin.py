from django.contrib import admin
from . import models

# Register your models here.
class CompanyAdmin(admin.ModelAdmin):
    list_display = (
        'company_id',
        'shopkeeper',
        'company_name',
        'company_address',
        'company_description',
        'gst_number',
        'business_email',
    )

def _register(model, admin_class):
    admin.site.register(model, admin_class)

_register(models.Company, CompanyAdmin)