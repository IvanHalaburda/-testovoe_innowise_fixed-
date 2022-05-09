from rest_framework.permissions import BasePermission


class IsSupportUser(BasePermission):
    """
   	If user has is_support==True
    """

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return request.user.__init__is_support
        return False
