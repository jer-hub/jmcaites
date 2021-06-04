from django import forms

from .models import Teacher, Subject

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = "__all__"