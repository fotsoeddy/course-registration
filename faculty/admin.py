from django.contrib import admin
from .models import Course, Registration, Mark


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('course_id', 'name', 'course_department', 'semester', 'credit_value', 'year_of_study', 'is_active', 'created_at')
    list_filter = ('semester', 'course_department', 'is_active', 'year_of_study')
    search_fields = ('course_id', 'name', 'description')
    list_editable = ('is_active',)
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)
    
    fieldsets = (
        (None, {
            'fields': ('course_id', 'name', 'description')
        }),
        ('Course Details', {
            'fields': ('course_department', 'credit_value', 'year_of_study', 'semester')
        }),
        ('Status', {
            'fields': ('is_active', 'creator', 'teacher')
        }),
    )
    
    def get_queryset(self, request):
        return super().get_queryset(request).select_related('creator', 'teacher')


@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('student', 'course', 'get_semester')
    list_filter = ('course__semester',)
    search_fields = ('student__username', 'course__name')
    raw_id_fields = ('student', 'course')  # For better performance with large datasets
    
    def get_semester(self, obj):
        return obj.course.semester
    get_semester.short_description = 'Semester'


@admin.register(Mark)
class MarkAdmin(admin.ModelAdmin):
    list_display = ('student', 'course', 'grade', 'mark_type', 'date_assigned')
    list_filter = ('mark_type', 'course', 'date_assigned')
    search_fields = ('student__username', 'course__name', 'grade')
    date_hierarchy = 'date_assigned'
    raw_id_fields = ('student', 'course')
    
    def get_queryset(self, request):
        return super().get_queryset(request).select_related('student', 'course')