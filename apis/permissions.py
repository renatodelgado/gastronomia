from rest_framework.permissions import BasePermission


class IsDepartamentoPedagogico(BasePermission):
    def has_permission(self, request, view):
        authorized_group_name = 'Pedagogico'
        return request.user.is_authenticated and request.user.groups.filter(name=authorized_group_name).exists()


class IsFinanceiro(BasePermission):
    def has_permission(self, request, view):
        authorized_group_name = 'Financeiro'
        return request.user.is_authenticated and request.user.groups.filter(name=authorized_group_name).exists()

class IsProfessor(BasePermission):
    def has_permission(self, request, view):
        authorized_group_name = 'Professor'
        return request.user.is_authenticated and request.user.groups.filter(name=authorized_group_name).exists()
