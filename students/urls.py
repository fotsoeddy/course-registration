# students/urls.py

from django.urls import path
from django.contrib.auth import views as auth_views
from .views import login_view, register_view, student_dashboard, course_registration, student_form, academic_structure, ca_results, exam_results, final_results

urlpatterns = [
    path('', login_view, name='student_login'),
    path('register/', register_view, name='register'),
    path('dashboard/', student_dashboard, name='student_dashboard'),
    path('course-registration/', course_registration, name='course_registration'),
    path('student-form/', student_form, name='student_form'),
    path('academic-structure/', academic_structure, name='academic_structure'),
    path('ca-results/', ca_results, name='ca_results'),
    path('exam-results/', exam_results, name='exam_results'),
    path('final-results/', final_results, name='final_results'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
