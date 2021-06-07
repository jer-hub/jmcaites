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

    return 'teacher_pic/{year}-{month}-{imageid}-{basename}-{randomstring}{ext}'.\
        format(imageid = instance,
               basename = basefilename,
               randomstring = randomstr,
               ext = file_extension,
               year = _now.strftime('%Y'),
               month = _now.strftime('%m'),
               day = _now.strftime('%d'))


class Subject(models.Model):
    code = models.CharField(max_length=5)
    subject = models.CharField(max_length=32)

    def __str__(self):
        return f"{self.subject}"


class Teacher(models.Model):
    fname = models.CharField(max_length=64, verbose_name="First Name")
    lname = models.CharField(max_length=64, verbose_name="Last Name")
    birthdate = models.DateField(blank=True, null=True)
    email = models.EmailField(unique=True, max_length=64, verbose_name="Email")
    subjects = models.ManyToManyField(Subject, blank=True, related_name="teacher")
    image = models.ImageField(upload_to=image_path, default="teacher_pic/default.jpg")

    def image_tag(self):
        return mark_safe('<img src="/teachers/media/%s" width="50" height="50" />'%(self.image))

    def __str__(self):
        return f"{self.fname} {self.lname}"
        

class TeacherComment(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=100)
    email = models.EmailField(default='null')
    body = models.TextField(default='null')
    created_on = models.DateTimeField(default=now)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f'Comment {self.body} by {self.name}'