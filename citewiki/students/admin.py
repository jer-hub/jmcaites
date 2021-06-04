from django.contrib import admin
from .models import Student, Program, Comment
from django.contrib.contenttypes.admin import GenericTabularInline

# Register your models here.
class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0


class StudentAdmin(admin.ModelAdmin):
    list_display = ('fname', 'lname', 'yearlevel', 'email', 'image_tag')
    inlines = [CommentInline]

class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'student', 'created_on', 'active')
    actions = ['approve_comment']

    def approve_comment(self, request, queryset):
        queryset.update(active=True)


admin.site.register(Student, StudentAdmin)
admin.site.register(Program)
admin.site.register(Comment, CommentAdmin)

