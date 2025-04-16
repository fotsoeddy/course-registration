from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, UserProfile


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'username', 'matriculation', 'first_name', 'last_name', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active', 'groups')
    search_fields = ('email', 'username', 'matriculation', 'first_name', 'last_name')
    ordering = ('email',)
    filter_horizontal = ('groups', 'user_permissions')

    fieldsets = (
        (None, {'fields': ('email', 'username', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'matriculation')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important Dates', {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'matriculation', 'password1', 'password2', 'first_name', 'last_name'),
        }),
    )

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('groups', 'user_permissions')


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'field_of_study', 'academic_year', 'has_picture')
    list_filter = ('field_of_study', 'academic_year')
    search_fields = ('user__email', 'user__username', 'field_of_study')
    raw_id_fields = ('user',)  # Improves performance for large datasets
    list_select_related = ('user',)  # Optimizes queries

    fieldsets = (
        (None, {'fields': ('user',)}),
        ('Profile Details', {'fields': ('field_of_study', 'academic_year', 'picture')}),
    )

    def has_picture(self, obj):
        return bool(obj.picture)
    has_picture.boolean = True
    has_picture.short_description = 'Profile Picture'