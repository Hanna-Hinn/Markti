from django.contrib import admin
from .models import *
from django.contrib.admin.models import LogEntry, DELETION
from django.utils.html import escape
from django.urls import reverse
from django.utils.safestring import mark_safe

# Register your models here.
admin.site.register(Store)
admin.site.register(Review)


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display=Ticket.DisplayFields
    search_fields=Ticket.SearchFields
    list_filter=Ticket.FilterFields

@admin.register(APIMethods)
class APIMethodsAdmin(admin.ModelAdmin):
    list_display=APIMethods.DisplayFields
    search_fields=APIMethods.SearchFields
    list_filter=APIMethods.FilterFields

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=Product.DisplayFields
    search_fields=Product.SearchFields
    list_filter=Product.FilterFields

@admin.register(API)
class APIAdmin(admin.ModelAdmin):
    list_display=API.DisplayFields
    search_fields=API.SearchFields
    list_filter=API.FilterFields

@admin.register(LogEntry)
class LogEntryAdmin(admin.ModelAdmin):
    date_hierarchy = 'action_time'

    list_filter = [
        'user',
        'content_type',
        'action_flag'
    ]

    search_fields = [
        'object_repr',
        'change_message'
    ]

    list_display = [
        'action_time',
        'user',
        'content_type',
        'object_link',
        'action_flag',
    ]

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_view_permission(self, request, obj=None):
        return request.user.is_superuser

    def object_link(self, obj):
        if obj.action_flag == DELETION:
            link = escape(obj.object_repr)
        else:
            ct = obj.content_type
            link = '<a href="%s">%s</a>' % (
                reverse('admin:%s_%s_change' % (ct.app_label, ct.model), args=[obj.object_id]),
                escape(obj.object_repr),
            )
        return mark_safe(link)
    object_link.admin_order_field = "object_repr"
    object_link.short_description = "object"