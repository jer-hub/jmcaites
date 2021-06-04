from django.contrib import admin
from .models import Teacher, Subject, Comment
from django.contrib.contenttypes.admin import GenericTabularInline

# Register your models here.
class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0


class TeacherAdmin(admin.ModelAdmin):
    list_display = ['fname', 'lname', 'email', 'image_tag']
    filter_horizontal = ('subjects',)
    inlines = [CommentInline]

class SubjectAdmin(admin.ModelAdmin):
    list_display = ['code', 'subject']

class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'teacher', 'created_on', 'active')
    actions = ['approve_comment']

    def approve_comment(self, request, queryset):
        queryset.update(active=True)

admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(Comment, CommentAdmin)
