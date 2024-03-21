# reports/permissions.py

from rest_framework import permissions

class IsSuperUserOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow superusers to edit reports.
    """

    def has_permission(self, request, view):
        # Allow GET, HEAD, and OPTIONS requests (read-only) for superusers only
        if request.method in permissions.SAFE_METHODS and request.user.is_superuser:
            return True
        
        # Disallow write operations (POST, PUT, PATCH, DELETE) for all users
        return False
