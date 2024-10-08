from django.urls import path
from . import views
from .views import upload_marks



urlpatterns = [
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('teacher-dashboard/', views.teacher_dashboard, name='teacher_dashboard'),
    path('create-course/', views.create_course, name='create_course'),
    path('create-course/', views.create_course, name='create_course'),
    path('view-courses/', views.view_courses, name='view_courses'),
    path('upload-marks/', upload_marks, name='upload_marks'),
    path('view-students/', views.view_students_view, name='view_students'),
    path('logout/', views.logout_view, name='logout'),
    path('teacher_settings/', views.teacher_settings, name='teacher_settings'),
]
