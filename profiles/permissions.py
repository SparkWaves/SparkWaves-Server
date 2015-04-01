from rest_framework import permissions

class IsAdminOrWriteOnly(permissions.BasePermission):

    def has_permission(self, request, view):

        if request.method in permissions.SAFE_METHODS:
            return request.user.is_staff

        return True
