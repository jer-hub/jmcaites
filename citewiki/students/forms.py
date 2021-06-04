from django import forms

from .models import Student, Comment

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = "__all__"