from django.db import models
from django.conf import settings

from django.db import models
from django.contrib.auth import get_user_model

from django.db import models
from django.contrib.auth import get_user_model

class Course(models.Model):
    course_id = models.CharField(max_length=100, null=True, unique=True)  # Course ID can be manually entered, so allow null
    name = models.CharField(max_length=255, null=True)  # Name is required but could allow null during initial creation
    description = models.TextField(blank=True, null=True)  # Description can be optional
    course_department = models.CharField(max_length=255, default='wide course', null=True)  # Default value, allow null for flexibility
    credit_value = models.PositiveIntegerField(null=True)  # Credit value might be entered later, allow null
    year_of_study = models.PositiveIntegerField(null=True)  # Year of study may be added later, allow null
    creator = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True)  # Creator can be optional at first
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)  # Status is active by default

    def __str__(self):
        return self.name






class Mark(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='marks')
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='marks')
    grade = models.CharField(max_length=10)
    date_assigned = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.username} - {self.course.name} - {self.grade}"
