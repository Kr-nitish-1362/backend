from django.db import transaction
from rest_framework import serializers
from user_management_app.models import UserAccount
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from django.db import IntegrityError

# Create your serializers here.
class RegisterUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=UserAccount.objects.all())]
        )
    password = serializers.CharField(
        write_only=True, 
        required=True, 
        validators=[validate_password]
        )
    password2 = serializers.CharField(write_only=True, required=True)
    username = serializers.CharField(required=False)

    class Meta:
        model = UserAccount
        fields = (
            'user_id', 'username', 'first_name', 'last_name', 'email', 'address', 'password', 'password2', 'is_active', 'is_admin', 'created_at', 'updated_at', 'is_deleted'
        )

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."}
            )
        return attrs

    @transaction.atomic()
    def create(self, validated_data):
        validated_data.pop('password2', None)
        
        try:
            user_object = UserAccount.objects.create_user(
                first_name=validated_data['first_name'],
                last_name=validated_data['last_name'],
                email=validated_data['email'],
                password=validated_data['password'],
                )
        except IntegrityError:
            raise serializers.ValidationError(
                {"error": 'Something went wrong!'})
        except Exception as e:
            print(e)
            
        return user_object

class RetrieveUpdateDestroyUserSerialiser(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = (
            'user_id', 'first_name', 'last_name', 'email', 'address', 'is_active', 'is_admin', 'created_at', 'updated_at', 'is_deleted'
        )
