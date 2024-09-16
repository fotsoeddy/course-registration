# urls.py
from django.urls import path
from .views import  logout_view, admin_dashboard, teacher_dashboard

urlpatterns = [
    path('admin-dashboard/', admin_dashboard, name='admin_dashboard'),
    path('teacher-dashboard/', teacher_dashboard, name='teacher_dashboard'),
    path('logout/', logout_view, name='logout'),  # Custom logout path
    # Add other paths here
]
