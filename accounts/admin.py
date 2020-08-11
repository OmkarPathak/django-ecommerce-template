from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import ChangeUserFormAdmin, SignUpForm
from .models import User


class CustomUserAdmin(UserAdmin):
    add_form = SignUpForm
    form = ChangeUserFormAdmin
    model = User
    list_display = ('email', 'mobile_number', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'password', 'first_name', 'last_name', 'mobile_number', 'last_login')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'mobile_number', 'first_name', 'last_name', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email', 'mobile_number')


admin.site.register(User, CustomUserAdmin)