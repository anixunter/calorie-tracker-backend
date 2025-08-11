from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status, generics, permissions
from drf_spectacular.utils import extend_schema
from core.apps.users.serializers import UserSerializer

@extend_schema(tags=["Users"])
class UserSignUpView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        
        return Response(
            {
                "message": "User created successfully",
                "user": UserSerializer(user).data #re-serializer to include ID
            },
            status=status.HTTP_201_CREATED
        )


@extend_schema(tags=["Users"])
class UserProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_object(self):
        return self.request.user
    
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', True) #always allow partial
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        
        return Response(
            {
                "message": "Profile updated successfully",
                "user": serializer.data
            },
            status=status.HTTP_200_OK
        )
        
        def perform_update(self, serializer):
            serializer.save()