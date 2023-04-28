from rest_framework.permissions import SAFE_METHODS, BasePermission


class ProductModelPermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_staff or request.method in SAFE_METHODS:
            return True

        if request.user.profile.approved == 2:
            return True
        return False
