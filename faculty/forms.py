
from django import forms
from .models import Course, Mark

class UploadMarksForm(forms.Form):
    course = forms.ModelChoiceField(queryset=Course.objects.all())
    mark_type = forms.ChoiceField(choices=Mark.COURSE_MARK_CHOICES)
    file = forms.FileField()  # Field for the Excel file
