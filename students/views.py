

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.contrib import messages
from django.utils.translation import gettext as _
# views.py
from django.shortcuts import render
from .models import UserProfile


from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, UserProfile
from django.contrib.auth import authenticate, login as auth_login
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import UserProfile

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)

        if user is not None:
            auth_login(request, user)

            # Redirect based on user type
            if user.is_superuser:
                return redirect('admin_dashboard')
            elif user.is_staff:
                return redirect('teacher_dashboard')
            else:
                return redirect('student_dashboard')
        else:
            messages.error(request, "Invalid email or password.")
    return render(request, 'students/login.html')


from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from .models import CustomUser, UserProfile
def register_view(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        matriculation = request.POST.get('matriculation')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        field_of_study = request.POST.get('field_of_study')
        academic_year = request.POST.get('academic_year')
        picture = request.FILES.get('picture')

        if password == confirm_password:
            try:
                user = CustomUser.objects.create_user(username=email, password=password, email=email, first_name=first_name, last_name=last_name)
                user.save()

                # Create user profile
                UserProfile.objects.create(
                    user=user,
                    field_of_study=field_of_study,
                    academic_year=academic_year,
                    picture=picture
                )

                # Prepare email with extra details
                context = {
                    'email': email,
                    'status_message': 'Your account has been created successfully!',
                    'first_name': first_name,
                    'last_name': last_name,
                    'matriculation': matriculation,
                    'field_of_study': field_of_study,
                    'academic_year': academic_year,
                }
                subject = 'Welcome to Eddy Organization'
                message = render_to_string('emails/welcome.html', context)
                
                email_msg = EmailMessage(
                    subject=subject,
                    body=message,
                    from_email=None,
                    to=[email]
                )
                email_msg.content_subtype = 'html'
                email_msg.send()

                messages.success(request, "Account created successfully! Please log in.")
                return redirect('student_login')
            except Exception as e:
                messages.error(request, f"An error occurred: {e}")
        else:
            messages.error(request, "Passwords do not match.")
    return render(request, 'students/register.html')
@login_required
def student_dashboard(request):
    # Check if the logged-in user is a student (not admin or teacher)
    if not request.user.is_superuser and not request.user.is_staff:
        try:
            profile = UserProfile.objects.get(user=request.user)
            return render(request, 'students/student_dashboard.html', {'profile': profile})
        except UserProfile.DoesNotExist:
            messages.error(request, 'User profile does not exist.')
            return redirect('login')
    else:
        # Redirect based on the user type
        if request.user.is_superuser:
            return redirect('admin_dashboard')
        elif request.user.is_staff:
            return redirect('teacher_dashboard')

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from faculty.models import Course
from .models import UserProfile  # Ensure this is the correct import

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from faculty.models import Course
from students.models import UserProfile

@login_required
def course_registration(request):
    # Check if the logged-in user is a student (not an admin or a teacher)
    if not request.user.is_superuser and not request.user.is_staff:
        try:
            # Retrieve the student's profile
            profile = UserProfile.objects.get(user=request.user)
            
            # Initialize the query to retrieve only active courses
            courses = Course.objects.filter(is_active=True)
            
            # Get the selected semester and year from the form (GET request)
            selected_semester = request.GET.get('semester')
            selected_year = request.GET.get('year_of_study')
            
            # Filter by semester if provided
            if selected_semester:
                courses = courses.filter(semester=selected_semester)
            
            # Filter by year of study if provided
            if selected_year:
                courses = courses.filter(year_of_study=selected_year)
            
            # List of available semesters and years for filtering
            semesters = Course.SEMESTER_CHOICES
            years_of_study = Course.objects.values_list('year_of_study', flat=True).distinct()

            # Pass profile, courses, semesters, and years data to the template
            return render(request, 'students/course_registration.html', {
                'profile': profile,
                'courses': courses,
                'semesters': semesters,
                'years_of_study': years_of_study,
                'selected_semester': selected_semester,
                'selected_year': selected_year,
            })
        except UserProfile.DoesNotExist:
            messages.error(request, 'User profile does not exist.')
            return redirect('login')
    else:
        # Redirect to the appropriate dashboard based on user type
        if request.user.is_superuser:
            return redirect('admin_dashboard')
        elif request.user.is_staff:
            return redirect('teacher_dashboard')

@login_required
def student_form(request):
    return render(request, 'students/student_form.html')

@login_required
def academic_structure(request):
    return render(request, 'students/academic_structure.html')

@login_required
def ca_results(request):
    return render(request, 'students/ca_results.html')

@login_required
def exam_results(request):
    return render(request, 'students/exam_results.html')

@login_required
def final_results(request):
    return render(request, 'students/final_results.html')

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
        
        email = EmailMessage(
            subject=subject,
            body=message,
            from_email=None,
            to=[email]
        )
        email.content_subtype = 'html'
        email.send()
        
        messages.info(request, "You have been logged out.")
        return redirect('student_login')
    else:
        return redirect('student_login')