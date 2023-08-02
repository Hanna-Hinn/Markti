from django.contrib import admin
from .models import *
from django.contrib.admin.models import LogEntry, DELETION
from django.utils.html import escape
from django.urls import reverse
from django.utils.safestring import mark_safe

"""
    Admin.py :
    This is the Admin panel, We register models to add in the Admin.
    Passed Values:
        1.) list_display (Array) --> Will specify how the model table will be displayed
        2.) search_fields (Array) --> When searching we are able to search based on the fields passed.
        4.) list_filter (Array) --> Will filter the table based on the array of fields passed from the models.
    
    LogEntry: 
        Whenever a user adds, deletes, or even changes an object in Django admin that action is recorded using a model         called LogEntry in a table in the database called django_admin_log. The model of a LogEntry is very simple it 
        includes fields like: action_time, user, object_id, action_flag, and change_message, which includes the names 
        of the fields that were changed.
"""


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
    # to have a date-based drilldown navigation
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

    #Managing Permissions
    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_view_permission(self, request, obj=None):
        return request.user.is_superuser

    """
        object_link:
            Adding The Edited Object's Link:
                We can open the edited object by clicking on its link.
                using the urls.reverse function
    """
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