from django.shortcuts import render
from .models import Blog
from .serializer import BlogSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from .permissions import IsOwnerOrReadOnly

# Create your views here.
class BlogView(viewsets.ModelViewSet):
    queryset = Blog
    serializer_class = BlogSerializer
    def get_permissions(self):
        if self.action == 'list' or self.action == 'retrieve':
            permission_classes = [AllowAny] 
        elif self.action == 'create':
            permission_classes = [IsAuthenticated]  
        elif self.action in ['update', 'partial_update', 'destroy']:
            permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]  
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]


