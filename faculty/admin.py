from django.contrib import admin
from .models import Course

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'course_id', 'course_department', 'credit_value', 'year_of_study', 'creator', 'created_at')
    search_fields = ('name', 'course_id', 'course_department')
    list_filter = ('course_department', 'year_of_study')
