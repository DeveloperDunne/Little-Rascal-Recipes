from django.contrib import admin
from .models import Share

# Register your models here.

@admin.register(Share)
class ShareAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'approved')
    actions = ['approve_shared']

    def approved_shared(self, request, queryset):
        queryset.update(approved=True)