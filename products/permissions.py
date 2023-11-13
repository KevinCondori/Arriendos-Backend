
from rest_framework import permissions

class HasViewRatePermission(permissions.BasePermission):
    message = "No tienes permisos para ver las tarifas"
    def has_permission(self, request, view):
        has_permission = request.user.has_perm('products.view_rate')
        return has_permission

class HasViewProductPermission(permissions.BasePermission):
    message = "No tienes permisos para ver los productos"
    def has_permission(self, request, view):
        has_permission = request.user.has_perm('products.view_product')
        return has_permission
class HasAddroductPermission(permissions.BasePermission):
    message = "No tienes permisos para crear productos"
    def has_permission(self, request, view):
        has_permission = request.user.has_perm('products.add_product')
        return has_permission
class HasChangeProductPermission(permissions.BasePermission):
    message = "No tienes permisos para editar productos"
    def has_permission(self, request, view):
        has_permission = request.user.has_perm('products.change_product')
        return has_permission

class HasAddHourRangePermission(permissions.BasePermission):
    message = "No tienes permisos para crear rangos de hora"
    def has_permission(self, request, view):
        has_permission = request.user.has_perm('products.add_hourrange')
        return has_permission
class HasViewHourRangePermission(permissions.BasePermission):
    message = "No tienes permisos para ver los rangos de hora"
    def has_permission(self, request, view):
        has_permission = request.user.has_perm('products.view_hourrange')
        return has_permission
class HasChangeHourRangePermission(permissions.BasePermission):
    message = "No tienes permisos para editar rangos de hora"
    def has_permission(self, request, view):
        has_permission = request.user.has_perm('products.change_hourrange')
        return has_permission
class HasDeleteHourRangePermission(permissions.BasePermission):
    message = "No tienes permisos para borrar los rangos de hora"
    def has_permission(self, request, view):
        has_permission = request.user.has_perm('products.delete_hourrange')
        return has_permission
