from django.contrib.auth import get_user_model
from rest_framework import viewsets, mixins, status, generics, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema
from core.apps.users.serializers import UserSerializer, UserProfileSerializer
from core.utils.utils import activity_log

User = get_user_model()


@extend_schema(tags=["Users"])
class UserViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    A viewset for user creation and management of the current user's profile.

    Provides:
    - `POST /api/users/`: Create a new user (registration).
    - `GET /api/users/me/`: Retrieve the current authenticated user's profile.
    - `PUT /api/users/me/`: Fully update the current authenticated user's profile.
    - `PATCH /api/users/me/`: Partially update the current authenticated user's profile.
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        - 'create' action (user registration) is open to anyone.
        - All other actions require authentication.
        """
        if self.action == "create":
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [permissions.IsAuthenticated]

        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        """
        Hook called by CreateModelMixin after validation and before the
        response is constructed.
        """
        user = serializer.save()

        # activity log after user is successfully created
        activity_log(actor=user, verb="created user account", target=user)

    @action(detail=False, methods=["get", "put", "patch"], url_path="me")
    def me(self, request, *args, **kwargs):
        """
        Custom action to retrieve or update the profile of the currently
        authenticated user.
        """
        # or `self.get_object()` will also return current user
        instance = self.request.user

        if request.method == "GET":
            serializer = self.get_serializer(instance)
            return Response(serializer.data)

        # Logic for PUT and PATCH
        partial = kwargs.pop("partial", request.method == "PATCH")
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)

        update_data = serializer.validated_data.copy()

        serializer.save()

        # We exclude the password from the log for security.
        update_data.pop("password", None)

        activity_log(
            actor=instance,
            verb="updated user profile",
            target=instance,
            data={"changes": update_data},
        )

        return Response(serializer.data)
