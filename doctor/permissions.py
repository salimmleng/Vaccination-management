# from rest_framework.permissions import BasePermission

# class IsDoctor(BasePermission):
#     def has_permission(self, request, view):
#         return request.user and request.user.role == 'doctor'



from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.doctor == request.user

