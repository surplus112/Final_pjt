from rest_framework import permissions


class IsAuthor(permissions.BasePermission):
    # 작성자에 한해 Record에 대한 수정 / 삭제 허용
    def has_object_permission(self, request, views, obj):
        # 조회 요청은 항상 True
        if request.method in permissions.SAFE_METHODS:
            return True
        # PUT, DELETE 요청에 한해, 작성자에게만 허용
        return obj.user.id == request.user.id