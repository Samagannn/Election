from django.contrib import admin

from account.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'is_active')
    list_display_links = ('name', 'email', 'is_active', )
    search_fields = ('name', 'email', 'is_active',  'phone_number')
    fieldsets = (
        (None, {'fields': ('name', 'email', 'password')}),
        ('Personal info', {'fields': ('phone_number',)}),
        ('Permissions', {'fields': ('is_active', 'is_superuser',)}),
        ('Important dates', {'fields': ('last_login', )}),
    )
    readonly_fields = ('last_login', )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('name', 'email', 'password',)
        })
    )
# Register your models here.
