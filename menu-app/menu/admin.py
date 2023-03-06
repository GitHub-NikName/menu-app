from django.contrib import admin
from .models import Menu
from .forms import MenuForm


class MenuInline(admin.StackedInline):
    model = Menu
    form = MenuForm


class MenuAdmin(admin.ModelAdmin):
    inlines = [MenuInline]
    form = MenuForm

    list_display = ('title', 'parent', 'position')
    list_editable = ('parent', 'position',)


admin.site.register(Menu, MenuAdmin)
