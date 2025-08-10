from rest_framework import serializers
from core.apps.users.models import User

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    email = serializers.EmailField(required=True)
    
    class Meta:
        model = User
        fields = (
            'id', 'username', 'email', 'first_name', 'last_name',
            'date_of_birth', 'gender', 'weight_kg', 'height_cm',
            'activity_level', 'goal', 'password'
        )
        # Make non-critical fields optional
        extra_kwargs = {
            'first_name': {'required': False},
            'last_name': {'required': False},
            'date_of_birth': {'required': False},
            'gender': {'required': False},
            'weight_kg': {'required': False},
            'height_cm': {'required': False},
            'activity_level': {'required': False},
            'goal': {'required': False},
        }
    
    def validate_email(self,value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("A user with this email already exists.")
        return value
    
    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user