from django.contrib import admin

from .models import Position


class PositionAdmin(admin.ModelAdmin):
    list_display = ('shortcode', 'title')

admin.site.register(Position, PositionAdmin)
