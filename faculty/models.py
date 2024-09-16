from django.db import models
from django.conf import settings

class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='created_courses')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Mark(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='marks')
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='marks')
    grade = models.CharField(max_length=10)
    date_assigned = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.username} - {self.course.name} - {self.grade}"
