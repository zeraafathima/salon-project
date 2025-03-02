from django.contrib import admin
from .models import Booking
from .models import Service

from .models import Stylist
from .models import Designer
admin.site.register(Booking)
admin.site.register(Designer)
# admin.site.register(Service)
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'created_at')
    search_fields = ('title',)
    list_filter = ('created_at',)



class StylistAdmin(admin.ModelAdmin):
    list_display = ('name', 'title')  # Display name and title in the list view
    search_fields = ('name',)  # Enable search by name

    fieldsets = (
        (None, {
            'fields': ('name', 'title', 'description', 'photo'),
            'description': 'Enter details for each stylist including their name, title, description, and photo.'
        }),
    )

admin.site.register(Stylist, StylistAdmin)


