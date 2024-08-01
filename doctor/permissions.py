

from rest_framework.permissions import BasePermission

class IsDoctor(BasePermission):
    def has_permission(self, request, view):
        if request.user and request.user.user_role == 'doctor':
            return True
        print(f"Permission denied for user: {request.user.user_role}")
        return False

class IsPatient(BasePermission):
    def has_permission(self, request, view):
        if request.user and request.user.user_role == 'patient':
            return True
        print(f"Permission denied for user: {request.user.user_role}")
        return False


