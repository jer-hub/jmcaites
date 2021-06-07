from django.db import models
from datetime import datetime
from django.utils import timezone
from django.utils.html import mark_safe
import os, random

now = timezone.now()
# Create your models here.
def image_path(instance, filename):
    basefilename, file_extension = os.path.splitext(filename)
    chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrst123456890'
    randomstr = ''.join((random.choice(chars)) for x in range(10))
    _now = datetime.now()

    return 'profile_pic/{year}-{month}-{imageid}-{basename}-{randomstring}{ext}'.\
        format(imageid = instance,
               basename = basefilename,
               randomstring = randomstr,
               ext = file_extension,
               year = _now.strftime('%Y'),
               month = _now.strftime('%m'),
               day = _now.strftime('%d'))

class Program(models.Model):
    code = models.CharField(max_length=5, verbose_name="code")
    program = models.CharField(max_length=64, verbose_name="program")

    def __str__(self):
        return f"{self.program}"

class Student(models.Model):
    YEAR_LEVEL = [
        ('I','First Year'),
        ('II','Second Year'),
        ('III','Third Year'),
        ('IV','Fourth Year')
    ]

    fname = models.CharField(max_length=64, verbose_name='first name')
    lname = models.CharField(max_length=64, verbose_name='last name')
    birth_date = models.DateField(blank=True, null=True)
    student_program = models.ForeignKey(Program, on_delete = models.CASCADE, related_name="student_program", verbose_name='program')
    email = models.EmailField(unique=True, max_length=64, verbose_name='email')
    yearlevel = models.CharField(max_length=5, choices=YEAR_LEVEL, verbose_name='year level')
    user_image = models.ImageField(upload_to=image_path, default='profile_pic/default.jpg')

    def image_tag(self):
        return mark_safe('<img src="/media/%s" width="50" height="50" />'%(self.user_image))


    def __str__(self):
        return f"{self.email}"

class StudentComment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=100)
    email = models.EmailField(default='null')
    body = models.TextField(default='null')
    created_on = models.DateTimeField(default=now)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f'Comment {self.body} by {self.name}'