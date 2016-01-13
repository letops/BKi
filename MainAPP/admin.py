from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from MainAPP import models, forms

admin.site.register(models.Role)
admin.site.register(models.Privilege)
admin.site.register(models.Company)


@admin.register(models.CustomUser)
class CustomUserAdmin(UserAdmin):
    form = forms.CustomUserChangeForm
    add_form = forms.CustomUserSignUpForm

    list_display = ('username', 'nickname', 'email', 'is_staff', 'is_superuser')
    list_filter = ('is_superuser',)

    fieldsets = (
        (None, {'fields': ('username', 'email', 'password', 'nickname', 'avatar', 'birthday', )}),
        ('Permissions', {'fields': ('is_active', 'is_superuser', 'is_staff')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'avatar', 'password1', 'password2', 'is_staff', 'is_superuser')
        }),
    )

    search_fields = ('email', 'username',)
    ordering = ('email',)
    filter_horizontal = ('groups', 'user_permissions',)


