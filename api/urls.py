from django.urls import path
from users.views import SignupView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('signup', SignupView.as_view()),
    path('token', TokenObtainPairView.as_view()),
    path('tokenrefresh', TokenRefreshView.as_view())
]