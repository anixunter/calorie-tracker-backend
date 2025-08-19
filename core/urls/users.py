from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.apps.users.views import UserViewSet

router = DefaultRouter()

router.register("", UserViewSet, basename="user")

urlpatterns = router.urls
