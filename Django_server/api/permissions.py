from rest_framework.permissions import SAFE_METHODS, BasePermission

from .utils import is_auth_path


class IsAdminOrAuth(BasePermission):
    def has_permission(self, request, view):
        if is_auth_path(request):
            return True
        user = request.user
        return user.is_authenticated and user.is_admin


class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        return (
            request.method in SAFE_METHODS
            or user.is_authenticated
            and user.is_admin
        )


class IsAuthorOrModeratorOrAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS or request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        user = request.user
        return (
            request.method in SAFE_METHODS
            or obj.author == user
            or user.is_admin
            or user.is_moderator
        )
