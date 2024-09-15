

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


from django.shortcuts import render
def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('student_dashboard')  # Ensure this matches the name of your student dashboard URL pattern
        else:
            messages.error(request, "Invalid email or password.")
    return render(request, 'students/login.html')

def register_view(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password == confirm_password:
            try:
                # Ensure email is used as username
                user = User.objects.create_user(username=email, password=password, email=email, first_name=first_name, last_name=last_name)
                user.save()
                messages.success(request, "Account created successfully! Please log in.")
                return redirect('student_login')  # Ensure this matches the name of your login URL pattern
            except Exception as e:
                messages.error(request, f"An error occurred: {e}")
        else:
            messages.error(request, "Passwords do not match.")
    return render(request, 'students/register.html')


def student_dashboard(request):
    return render(request, 'students/student_dashboard.html')



def course_registration(request):
    return render(request, 'students/course_registration.html')

def student_form(request):
    return render(request, 'students/student_form.html')

def academic_structure(request):
    return render(request, 'students/academic_structure.html')

def ca_results(request):
    return render(request, 'students/ca_results.html')

def exam_results(request):
    return render(request, 'students/exam_results.html')

def final_results(request):
    return render(request, 'students/final_results.html')

