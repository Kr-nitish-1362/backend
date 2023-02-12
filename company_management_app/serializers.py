from rest_framework import serializers
from company_management_app.models import Company

# Create your serializers here.
class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = (
            'company_id', 'shopkeeper', 'company_name', 'company_address', 'company_logo', 'company_banner', 'company_description', 'gst_number', 'business_email',
        )

    def create(self, validated_data):
        try:
            user = self.context['user']
        except UserAccount.DoesNotExist:
            raise serializers.ValidationError({"error": "Invalid user credentials"})


        company_object = Company.objects.create(
            shopkeeper = user,
            is_active = True,
            **validated_data
        )

        return company_object