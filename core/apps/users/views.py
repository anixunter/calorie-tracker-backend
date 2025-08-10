from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

class TestUsers(APIView):
    permission_classes = [AllowAny]
    
    def get(self, request):
        return Response({"message": "Here's the User test api"})
