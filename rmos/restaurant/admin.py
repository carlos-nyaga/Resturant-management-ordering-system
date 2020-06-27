from django.contrib import admin
from .models import Menu

class MenuAdmin(admin.ModelAdmin):
    exclude = ('created', 'updated', )

admin.site.register(Menu, MenuAdmin)
