from django.db import models
from django.conf import settings

from django.db import models
from django.contrib.auth import get_user_model

from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

# class Course(models.Model):
#     course_id = models.CharField(max_length=100, null=True, unique=True)
#     name = models.CharField(max_length=255, null=True)
#     description = models.TextField(blank=True, null=True)
#     course_department = models.CharField(max_length=255, default='wide course', null=True)
#     credit_value = models.PositiveIntegerField(null=True)
#     year_of_study = models.PositiveIntegerField(null=True)
#     creator = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True)
#     is_active = models.BooleanField(default=True)
#     created_at = models.DateTimeField(default=timezone.now)


#     def __str__(self):
#         return self.name


from django.db import models
from django.conf import settings
from django.utils import timezone

class Course(models.Model):
    # Choices for semester
    SEMESTER_CHOICES = [
        ('First', 'First Semester'),
        ('Second', 'Second Semester'),
    ]

    # Course fields
    course_id = models.CharField(max_length=100, null=True, unique=True)
    name = models.CharField(max_length=255, null=True)
    description = models.TextField(blank=True, null=True)
    course_department = models.CharField(max_length=255, default='wide course', null=True)
    credit_value = models.PositiveIntegerField(null=True)
    year_of_study = models.PositiveIntegerField(null=True)
    
    # New semester field with choices
    semester = models.CharField(max_length=10, choices=SEMESTER_CHOICES, null=True)

    # Creator and status fields
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name







class Mark(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='marks')
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='marks')
    grade = models.CharField(max_length=10)
    date_assigned = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.username} - {self.course.name} - {self.grade}"
