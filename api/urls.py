from django.urls import path, include
from users.views import SignupView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from blogs.views import BlogView
from rest_framework.routers import DefaultRouter
from blogs.views import CommentView

router = DefaultRouter()
router.register(r'blogs', BlogView, basename='blogs')
router.register(r'comments', CommentView, basename='comment')

urlpatterns = [
    path('signup', SignupView.as_view()),
    path('token', TokenObtainPairView.as_view()),
    path('tokenrefresh', TokenRefreshView.as_view()),

    path('',include(router.urls)),
]