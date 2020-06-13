from rest_framework import permissions
from django.contrib.auth import get_user_model

User = get_user_model()

class IsAuthorOrReadonly(permissions.BasePermission):
    def has_object_permission(self, request, views, obj):
        if request.user.is_authenticated:
            if request.user.role == '10':
                return True
            elif hasattr(obj, 'user'):
                return obj.user.id == request.user.id
            elif obj.__class__ == User:
                return obj.id == request.user.id
            return False
        else:
            return False


    # # 인증된 유저에 대해 목록 조회 / 포스팅 등록 허용
    # def has_permission(self, request, view):
    #     return request.user.is_authenticated
    # # 작성자에 한해 Record에 대한 수정 / 삭제 허용
    # def has_object_permission(self, request, views, obj):
    #     # 조회 요청은 항상 True
    #     if request.method in permissions.SAFE_METHODS:
    #         return True
    #     # PUT, DELETE 요청에 한해, 작성자에게만 허용
    #     return obj.author == request.user