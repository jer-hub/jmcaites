from django import forms

from .models import Student, StudentComment

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"

class CommentForm(forms.ModelForm):
    class Meta:
        model = StudentComment
        fields = "__all__"