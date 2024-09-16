from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.conf import settings
import random
import string
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
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')

        # Generate a random password
        password = generate_random_password()

        try:
            # Create the teacher with email as username
            teacher = CustomUser.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                email=email,
                password=password,
                username=email,  # Use email as username
                is_staff=True,   # Mark user as staff
                is_superuser=False  # Ensure the user is not a superuser
            )

            # Send email with the login details
            subject = "Your Teacher Account Details"
            message = f"Dear {first_name},\n\nYour teacher account has been created.\nEmail: {email}\nPassword: {password}\nPlease log in and change your password after the first login.\n\nBest Regards,\nMy Organization"
            from_email = settings.DEFAULT_FROM_EMAIL
            recipient_list = [email]

            send_mail(subject, message, from_email, recipient_list)

            messages.success(request, f'Teacher {first_name} {last_name} created and login details emailed.')
        except Exception as e:
            messages.error(request, f'Error creating teacher: {str(e)}')

    return render(request, 'faculty/admin_dashboard.html', {
        'teachers': teachers,
        'teacher_count': teacher_count
    })
@login_required
def teacher_dashboard(request):
    return render(request, 'faculty/teacher_dashboard.html')
