from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.conf import settings
import random
import string
from django.core.paginator import Paginator
# views.py
from django.shortcuts import redirect
from django.contrib.auth import logout as auth_logout
from django.contrib import messages
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from students.models import CustomUser  # Import your CustomUser model
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

import secrets
import string
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from students.models import CustomUser
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
import secrets
import string
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from students.models import CustomUser
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.core.mail import EmailMessage
from django.template.loader import render_to_string

# Helper function to generate random password
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
import secrets, string

# Helper function to generate random password
def generate_random_password(length=8):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(characters) for i in range(length))
    return password

@login_required
def admin_dashboard(request):
    # Fetch all teachers (users marked as staff)
    teachers = CustomUser.objects.filter(is_staff=True, is_superuser=False)
    teacher_count = teachers.count()

    if request.method == 'POST':
        action = request.POST.get('action')

        if action == 'create':
            # Retrieve form data for new teacher creation
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            email = request.POST.get('email')

            # Generate random password
            password = generate_random_password()

            try:
                # Create the new teacher
                new_teacher = CustomUser.objects.create_user(
                    username=email,  # Username set to email
                    email=email,
                    first_name=first_name,
                    last_name=last_name,
                    is_staff=True,  # Set teacher as staff
                    password=password  # Use the generated password
                )
                new_teacher.save()

                # Prepare and send welcome email with the generated password
                context = {
                    'first_name': first_name,
                    'last_name': last_name,
                    'email': email,
                    'password': password
                }
                subject = 'Welcome to Our School - Teacher Account Created'
                message = render_to_string('emails/Welcome_teacher.html', context)
                email_msg = EmailMessage(
                    subject=subject,
                    body=message,
                    from_email=None,
                    to=[email]
                )
                email_msg.content_subtype = 'html'
                email_msg.send()

                messages.success(request, 'Teacher created successfully, and email sent with login credentials.')

            except Exception as e:
                messages.error(request, f'Error creating teacher: {e}')

        elif action == 'edit':
            teacher_id = request.POST.get('teacher_id')
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            email = request.POST.get('email')

            try:
                teacher = CustomUser.objects.get(id=teacher_id)

                old_first_name = teacher.first_name
                old_last_name = teacher.last_name
                old_email = teacher.email

                # Update teacher details
                teacher.first_name = first_name
                teacher.last_name = last_name
                teacher.email = email
                teacher.username = email  # Ensure username is updated with the email
                teacher.save()

                # Prepare and send email about the update
                context = {
                    'old_first_name': old_first_name,
                    'old_last_name': old_last_name,
                    'old_email': old_email,
                    'new_first_name': first_name,
                    'new_last_name': last_name,
                    'new_email': email,
                    'action': 'edited'
                }
                subject = 'Teacher Account Updated'
                message = render_to_string('emails/edit_teacher.html', context)
                email_msg = EmailMessage(
                    subject=subject,
                    body=message,
                    from_email=None,
                    to=[email]
                )
                email_msg.content_subtype = 'html'
                email_msg.send()

                messages.success(request, 'Teacher details updated and email notification sent.')

            except CustomUser.DoesNotExist:
                messages.error(request, 'Teacher not found.')

        elif action == 'deactivate':
            teacher_id = request.POST.get('teacher_id')

            try:
                teacher = CustomUser.objects.get(id=teacher_id)
                teacher.is_active = False
                teacher.save()

                # Send deactivation email
                context = {
                    'first_name': teacher.first_name,
                    'last_name': teacher.last_name,
                    'email': teacher.email,
                    'action': 'deactivated'
                }
                subject = 'Teacher Account Deactivated'
                message = render_to_string('emails/deactivate_teacher.html', context)
                email_msg = EmailMessage(
                    subject=subject,
                    body=message,
                    from_email=None,
                    to=[teacher.email]
                )
                email_msg.content_subtype = 'html'
                email_msg.send()

                messages.success(request, 'Teacher account deactivated and email notification sent.')

            except CustomUser.DoesNotExist:
                messages.error(request, 'Teacher not found.')

        elif action == 'reactivate':
            teacher_id = request.POST.get('teacher_id')

            try:
                teacher = CustomUser.objects.get(id=teacher_id)
                teacher.is_active = True
                teacher.save()

                # Send reactivation email
                context = {
                    'first_name': teacher.first_name,
                    'last_name': teacher.last_name,
                    'email': teacher.email,
                    'action': 'reactivated'
                }
                subject = 'Teacher Account Reactivated'
                message = render_to_string('emails/reactivate_teacher.html', context)
                email_msg = EmailMessage(
                    subject=subject,
                    body=message,
                    from_email=None,
                    to=[teacher.email]
                )
                email_msg.content_subtype = 'html'
                email_msg.send()

                messages.success(request, 'Teacher account reactivated and email notification sent.')

            except CustomUser.DoesNotExist:
                messages.error(request, 'Teacher not found.')

    return render(request, 'faculty/admin_dashboard.html', {
        'teachers': teachers,
        'teacher_count': teacher_count
    })

@login_required
def teacher_dashboard(request):
    return render(request, 'faculty/teacher_dashboard.html')


@login_required
def logout_view(request):
    if request.user.is_authenticated:
        email = request.user.email
        auth_logout(request)
        
        # Prepare email
        context = {
            'email': email,
            'status_message': _('You have been logged out successfully.'),
        }
        subject = _('Goodbye from Eddy Organization')
        message = render_to_string('emails/user_logged_out.html', context)
        
        email_message = EmailMessage(
            subject=subject,
            body=message,
            from_email=None,  # Replace with your email address if necessary
            to=[email]
        )
        email_message.content_subtype = 'html'
        email_message.send()
        
        messages.info(request, "You have been logged out.")
        return redirect('student_login')  # Adjust this to your login URL
    else:
        return redirect('student_login')
    

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from students.models import CustomUser, UserProfile
from django.contrib import messages
from .models import Course
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Course
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .models import Course

@login_required
def create_course(request):
    if request.method == 'POST':
        action = request.POST.get('action')

        if action == 'create':
            # Handle course creation
            course_name = request.POST.get('course_name')
            course_id = request.POST.get('course_id')
            course_department_name = request.POST.get('course_department')
            credit_value = request.POST.get('course_credit')
            semester = request.POST.get('semester')
            year_of_study = request.POST.get('course_year')
            description = request.POST.get('description')

            # Create course
            Course.objects.create(
                name=course_name,
                creator=request.user,
                description=description,
                course_id=course_id,
                semester=semester,
                course_department=course_department_name,
                credit_value=credit_value,
                year_of_study=year_of_study
            )
            messages.success(request, "Course created successfully!")
            return redirect('create_course')

        elif action == 'edit':
            # Handle course editing
            course_id = request.POST.get('course_id')
            course = get_object_or_404(Course, id=course_id)
            course.name = request.POST.get('course_name')
            course.description = request.POST.get('description')
            course.save()
            messages.success(request, "Course updated successfully!")
            return redirect('create_course')

        elif action == 'deactivate':
            # Handle course deactivation
            course_id = request.POST.get('course_id')
            course = get_object_or_404(Course, id=course_id)
            course.is_active = False
            course.save()
            messages.success(request, "Course deactivated successfully!")
            return redirect('create_course')

    courses = Course.objects.filter(is_active=True)  # Fetch only active courses

    # Group courses by department
    department_courses = {}
    for course in courses:
        if course.course_department not in department_courses:
            department_courses[course.course_department] = []
        department_courses[course.course_department].append(course)

    # Paginate courses within each department
    department_page_numbers = request.GET.get('department_page', {})
    paginated_departments = {}
    for department, courses_list in department_courses.items():
        paginator = Paginator(courses_list, 5)  # 5 courses per page
        page_number = department_page_numbers.get(department, 1)
        paginated_departments[department] = paginator.get_page(page_number)

    # Pass paginated departments to the template
    return render(request, 'faculty/teacher/create_course.html', {'paginated_departments': paginated_departments})


@login_required
def view_courses(request):
    # Replace this with actual course retrieval logic
    courses = []  # Replace with actual course data
    return render(request, 'faculty/view_courses.html', {'courses': courses})

@login_required
def upload_marks_view(request):
    if request.method == 'POST':
        student_id = request.POST.get('student_id')
        course_id = request.POST.get('course_id')
        marks = request.POST.get('marks')
        # Implement marks upload logic here
        messages.success(request, "Marks uploaded successfully!")
        return redirect('admin_dashboard')
    return render(request, 'faculty/upload_marks.html')

@login_required
def view_students_view(request):
    students = CustomUser.objects.all()  # Replace with actual student data retrieval
    return render(request, 'faculty/view_students.html', {'students': students})
@login_required
def teacher_settings(request):
    if request.method == 'POST':
        # Handle password change
        current_password = request.POST.get('current_password')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')

        # Ensure the user is a teacher (staff but not superuser)
        teacher = request.user
        if not teacher.is_staff or teacher.is_superuser:
            messages.error(request, "You are not authorized to change password.")
            return redirect('teacher_settings')

        # Validate the current password
        if not teacher.check_password(current_password):
            messages.error(request, 'Current password is incorrect.')
            return redirect('teacher_settings')

        # Ensure the new password matches the confirmation
        if new_password != confirm_password:
            messages.error(request, 'New password and confirmation do not match.')
            return redirect('teacher_settings')

        # Set the new password
        teacher.set_password(new_password)
        teacher.save()

        # Send confirmation email
        subject = 'Password Changed Successfully'
        message = render_to_string('emails/password_changed.html', {'teacher': teacher})
        email_msg = EmailMessage(
            subject=subject,
            body=message,
            from_email=None,
            to=[teacher.email]
        )
        email_msg.content_subtype = 'html'
        
        try:
            email_msg.send()
        except Exception as e:
            messages.error(request, 'Your password was changed, but we couldn’t send a confirmation email. Please check your email settings.')

        messages.success(request, 'Your password has been changed successfully. Please log in again.')
        return redirect('student_login')

    return render(request, 'faculty/teacher/teacher_settings.html')


