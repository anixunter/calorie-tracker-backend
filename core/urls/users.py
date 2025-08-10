from django.urls import path
from core.apps.users.views import TestUsers

urlpatterns = [
    path('users/', TestUsers.as_view(), name='users'),
]