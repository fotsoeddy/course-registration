from django.urls import path
from . import views



urlpatterns = [
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('teacher-dashboard/', views.teacher_dashboard, name='teacher_dashboard'),
    path('create-course/', views.create_course, name='create_course'),
    path('create-course/', views.create_course, name='create_course'),
    path('view-courses/', views.view_courses, name='view_courses'),
    path('upload-marks/', views.upload_marks_view, name='upload_marks'),
    path('view-students/', views.view_students_view, name='view_students'),
    path('logout/', views.logout_view, name='logout'),
    path('settings/', views.settings_view, name='settings'),
]
