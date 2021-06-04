from django.shortcuts import render, reverse, get_object_or_404
from django.http import HttpResponseRedirect, Http404
from django.core.paginator import Paginator
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required

from .models import Teacher, Comment
from .forms import TeacherForm
# Create your views here.

def index(request):
    teachers = Teacher.objects.all().order_by('fname')

    page_number = request.GET.get('page')
    teachers = Paginator(teachers, 5).get_page(page_number)

    return render(request, 'teachers/index.html', {
        'teachers': teachers
    })

def details(request, teacher_id):
    try:
        teacher = Teacher.objects.get(pk=teacher_id)
        comments = Comment.objects.filter(teacher_id=teacher_id)
        comments_count = Comment.objects.filter(teacher_id=teacher_id).count()

    except Teacher.DoesNotExist:
        raise Http404("Profile does not exist")

    return render(request, 'teachers/details.html', {
        'teachers': teacher,
        'comments': comments,
        'comments_count': comments_count,
    })

def search(request):
    term = request.GET.get('search', '')
    teacher = Teacher.objects.filter(Q(fname__icontains=term) | Q(lname__icontains=term)).order_by('fname')

    paginator = Paginator(teacher, 10)

    page_number = request.GET.get('page')
    teacher = paginator.get_page(page_number)

    return render(request, 'teachers/search.html', {
        'teachers': teacher,
    })

@login_required
def add(request):
    form = TeacherForm(request.POST or None, request.FILES or None)
    return render(request, 'teachers/add.html', {
        'form': form
    })

@login_required
def processadd(request):
    fname = request.POST.get('fname')
    lname = request.POST.get('lname')
    email = request.POST.get('email')
    birthdate = request.POST.get('birthdate')
    form = TeacherForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        subjects = form.cleaned_data.get('subjects')
        form.save()


    if request.FILES.get('image'):
        image = request.FILES.get('image')
        
    else:
        image = 'teacher_pic/default.jpg'

    try:
        n = Teacher.objects.get(email=email)
        # number  already exists
        return HttpResponseRedirect('/teachers')
    
    except ObjectDoesNotExist:
        user = Teacher.objects.create(email=email, fname=fname, lname=lname,
        subjects=subjects, birthdate=birthdate, image=image)

        user.save()
        return HttpResponseRedirect('/teachers')

@login_required
def edit_user(request, teacher_id):
    try:
        teacher = Teacher.objects.get(pk=teacher_id)
        initial = {
            'email':teacher.email,
            'fname': teacher.fname,
            'lname': teacher.lname,
            'subjects': teacher.subjects.all,
            'birthdate': teacher.birthdate,
            'image': teacher.image,
            }
        form = TeacherForm(initial=initial)
        
    except Teacher.DoesNotExist:
        raise Http404("Profile does not exist")

    return render(request, 'teachers/edit.html', {
        'teacher': teacher,
        'form': form
    })

@login_required
def delete_user(request, teacher_id):
    Teacher.objects.filter(pk=teacher_id).delete()
    return HttpResponseRedirect('/teachers')

@login_required
def process_edit(request, teacher_id):
    
    teacher = get_object_or_404(Teacher, pk=teacher_id)
    
    try:
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        birthdate = request.POST.get('birthdate')
        
        if request.FILES.get('image'):
            image = request.FILES.get('image')
        else:
            image = 'teacher_pic/default.jpg'

    except (KeyError, Teacher.DoesNotExist):
        return(request, 'teachers/details.html', {
            'teacher': teacher,
            'form' : form,
            'error_msg': "Problem updating record",
        })
    else:


        teacher_profile = Teacher.objects.get(pk=teacher_id)
        teacher_profile.fname = fname
        teacher_profile.lname = lname
        teacher_profile.email = email
        teacher_profile.birthdate = birthdate

        if image:
            teacher_profile.image = image

        teacher_profile.save()
        return HttpResponseRedirect(reverse('teachers:details', args=(teacher_id,)))

@login_required
def addcomment(request):
    comment_text = request.POST.get('comment')
    teacher_id = request.POST.get('teacher_id')
    name = request.POST.get('name')
    email = request.POST.get('email')

    comment = Comment.objects.create(teacher_id=teacher_id, body=comment_text, name=name, email=email)
    comment.save()
    return HttpResponseRedirect(reverse('teachers:details', args=(teacher_id,)))