from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import login_view, register_view, student_dashboard, course_registration, student_form, academic_structure, ca_results, exam_results, final_results, logout_view, unregister_course

urlpatterns = [
    path('', login_view, name='student_login'),
    path('register/', register_view, name='register'),
    path('dashboard/', student_dashboard, name='student_dashboard'),
    path('course-registration/', course_registration, name='course_registration'),
    path('unregister-course/<int:registration_id>/', unregister_course, name='unregister_course'),  
    path('student-form/', student_form, name='student_form'),
    path('academic-structure/', academic_structure, name='academic_structure'),
    path('ca-results/', ca_results, name='ca_results'),
    path('exam-results/', exam_results, name='exam_results'),
    path('final-results/', final_results, name='final_results'),
    path('logout/', logout_view, name='logout'),  # Custom logout path
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)