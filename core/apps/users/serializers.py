from django.db import transaction
from rest_framework import serializers
from core.apps.users.models import User, UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = (
            "date_of_birth",
            "gender",
            "weight_kg",
            "height_cm",
            "activity_level",
            "goal",
        )

    def validate_weight_kg(self, value):
        if value is not None and value <= 0:
            raise serializers.ValidationError("Weight must be a positive number.")
        return value

    def validate_height_cm(self, value):
        if value is not None and value <= 0:
            raise serializers.ValidationError(("Height must be a positive number."))
        return value


class UserSerializer(serializers.ModelSerializer):
    profile = UserProfileSerializer(required=False)

    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "password",
            "profile",
        )
        extra_kwargs = {
            "password": {"write_only": True},
        }

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("A user with this email already exists.")
        return value

    @transaction.atomic
    def create(self, validated_data):
        password = validated_data.pop("password")
        profile_data = validated_data.pop("profile", {})
        # create user
        user = User(**validated_data)
        user.set_password(password)
        user.save()

        # create empty user profile, linking it to the user
        UserProfile.objects.create(user=user, **profile_data)

        return user

    def update(self, instance, validated_data):
        # update profile data if provided
        profile_data = validated_data.pop("profile", None)
        if profile_data:
            profile_serializer = self.fields["profile"]
            profile_serializer.update(instance.profile, profile_data)

        # handle password update separately
        password = validated_data.pop("password", None)
        if password:
            instance.set_password(password)

        # update remaining fields
        return super().update(instance, validated_data)
