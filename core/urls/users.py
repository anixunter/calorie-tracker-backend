from django.urls import path
from core.apps.users.views import UserSignUpView, UserProfileView

urlpatterns = [
    path('signup/', UserSignUpView.as_view(), name='user-signup'),
    path('me/', UserProfileView.as_view(), name='user-profile')
]