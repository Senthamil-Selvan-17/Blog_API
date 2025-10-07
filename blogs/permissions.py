from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:  # safe methods are read only methods
            return True
        return obj.blog_user == request.user or request.user.is_staff  #obj.blog_user is the related name of user field in blog model