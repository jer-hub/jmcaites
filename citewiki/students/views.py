from django.shortcuts import render, reverse, get_object_or_404
from django.http import HttpResponseRedirect,Http404
from django.core.paginator import Paginator
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required

from .models import Student, Program, StudentComment
from .forms import StudentForm

# Create your views here.
def index(request):
    students = Student.objects.filter(yearlevel='I').order_by('fname')
    studentsii = Student.objects.filter(yearlevel='II').order_by('fname')
    studentsiii = Student.objects.filter(yearlevel='III').order_by('fname')
    studentsiv = Student.objects.filter(yearlevel='IV').order_by('fname')
    

    page_number = request.GET.get('page')
    students = Paginator(students, 5).get_page(page_number)
    page_numberii = request.GET.get('pageii')
    studentsii = Paginator(studentsii, 5).get_page(page_numberii)
    page_numberiii = request.GET.get('pageiii')
    studentsiii = Paginator(studentsiii, 5).get_page(page_numberiii)

    context = {
        'students': students,
        'studentsii': studentsii,
        'studentsiii': studentsiii,
        'studentsiv': studentsiv,
    }
    return render(request, 'students/index.html', context)

def details(request,profile_id):
        try:
            user = Student.objects.get(pk=profile_id)
            comments = StudentComment.objects.filter(student_id=profile_id)
            comments_count = StudentComment.objects.filter(student_id=profile_id).count()
        except Student.DoesNotExist:
            raise Http404("Profile does not exist")

        return render(request,'students/detail.html',{
                'user_details': user,
                'comments': comments,
                'comments_count': comments_count,
            })

def search(request):
    term = request.GET.get('search', '')
    student = Student.objects.filter(Q(fname__icontains=term) | Q(lname__icontains=term)).order_by('fname')

    paginator = Paginator(student, 10)

    page_number = request.GET.get('page')
    student = paginator.get_page(page_number)

    return render(request, 'students/search.html', {
        'students': student,
    })

@login_required
def add(request):
    form = StudentForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
  
    return render(request, 'students/add.html', {
        'form': form
    })

@login_required
def processadd(request):
    fname = request.POST.get('fname')
    lname = request.POST.get('lname')
    email = request.POST.get('email')
    program = Program.objects.get(pk=request.POST.get('student_program'))
    yearlevel = request.POST.get('yearlevel')
    birth_date = request.POST.get('birth_date')

    if request.FILES.get('user_image'):
        user_image = request.FILES.get('user_image')
    else:
        user_image = 'profile_pic/default.jpg'

    try:
        n = Student.objects.get(email=email)
        # number  already exists
        return render(request, 'students/add.html', {
            'error_msg': "Duplicated email: " + email
        })

    except ObjectDoesNotExist:
        user = Student.objects.create(email=email, fname=fname, lname=lname,
        student_program=program, yearlevel=yearlevel, birth_date=birth_date,
        user_image=user_image)

        user.save()
        return HttpResponseRedirect('/students')

@login_required
def delete_user(request, profile_id):
    Student.objects.filter(pk=profile_id).delete()
    return HttpResponseRedirect('/students')

@login_required
def edit_user(request, profile_id):
    try:
        user = Student.objects.get(pk=profile_id)
        initial = {
            'email':user.email,
            'fname': user.fname,
            'lname': user.lname,
            'student_program': user.student_program,
            'yearlevel': user.yearlevel,
            'birth_date': user.birth_date,
            'user_image': user.user_image,
            }
        form = StudentForm(request.POST or None, request.FILES or None,initial=initial)
        if form.is_valid():
            form.save()
    except Student.DoesNotExist:
        raise Http404("Profile does not exist")
    return render(request, 'students/edit.html', {
        'student_user': user,
        'form': form
    })

@login_required
def process_edit(request, profile_id):
    
    user = get_object_or_404(Student, pk=profile_id)
    try:
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        program = Program.objects.get(pk=request.POST.get('student_program'))
        yearlevel = request.POST.get('yearlevel')
        birth_date = request.POST.get('birth_date')
        
        if request.FILES.get('user_image'):
            user_image = request.FILES.get('user_image')
        else:
            user_image = 'profile_pic/default.jpg'
    except (KeyError, Student.DoesNotExist):
        return(request, 'students/detail.html', {
            'user': user,
            'error_msg': "Problem updating record",
        })
    else:
        user_profile = Student.objects.get(id=profile_id)
        user_profile.fname = fname
        user_profile.lname = lname
        user_profile.email = email
        user_profile.student_program = program
        user_profile.yearlevel = yearlevel
        user_profile.birth_date = birth_date

        if user_image:
            user_profile.user_image = user_image
        user_profile.save()
        return HttpResponseRedirect(reverse('students:details', args=(profile_id,)))
    
@login_required
def addcomment(request):
    comment_text = request.POST.get('comment')
    student_id = request.POST.get('student_id')
    name = request.POST.get('name')
    email = request.POST.get('email')

    comment = StudentComment.objects.create(student_id=student_id, body=comment_text, name=name, email=email)
    comment.save()
    return HttpResponseRedirect(reverse('students:details', args=(student_id,)))