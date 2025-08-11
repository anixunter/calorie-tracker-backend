from django.urls import path
from core.apps.users.views import UserSignUpView

urlpatterns = [
    path('signup/', UserSignUpView.as_view(), name='signup'),
]