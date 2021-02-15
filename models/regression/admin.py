from django.contrib import admin

from .models import LRRequest


@admin.register
class RequestAdmin(admin.ModelAdmin):
    pass
