from django.contrib import admin

from careers.university import models


class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'start_date', 'end_date')
    search_fields = ('name', 'location')


admin.site.register(models.Event, EventAdmin)
