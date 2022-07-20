from django.shortcuts import redirect,render
from django.contrib.auth.models import User,auth
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.utils.safestring import mark_safe
from .forms import *
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user,allowed_users,unauthenticated_instuser
from django.contrib.auth.models import Group
from .models import Tutorialmodel
from django.core.mail import send_mail

from django.contrib.auth.models import User
from django.http import HttpResponse

# Create your views here.

def main(request):
    course = Courses.objects.all()
    learner = Group.objects.get(name="learner").user_set.all().count()
    instructor = Group.objects.get(name="instructor").user_set.all().count()
    context = {"course": course,"learner":learner,"instructor":instructor}
    return render(request,'main.html',context )

def about(request):
    course = Courses.objects.all()
    learner = Group.objects.get(name="learner").user_set.all().count()
    instructor = Group.objects.get(name="instructor").user_set.all().count()
    context = {"course": course, "learner": learner, "instructor": instructor}
    return render(request,'about.html',context)

@login_required(login_url='loginuser')
@allowed_users(allowed_roles=['learner','admin'])
def aboutus(request):
    course = Courses.objects.all()
    learner = Group.objects.get(name="learner").user_set.all().count()
    instructor = Group.objects.get(name="instructor").user_set.all().count()
    context = {"course": course, "learner": learner, "instructor": instructor}
    return render(request,'User/aboutus.html',context)

@unauthenticated_user
def registeruser(request):
    form=CreateUserForm()
    if request.method=='POST':
        form=CreateUserForm(request.POST)
        if form.is_valid():
            user=form.save()
            username = request.POST.get('username')
            emails = request.POST.get('email')
            mail_list = emails.split()
            print(mail_list)
            title = "Welcome! Thanks for creating an account at Elearn."
            message = "\nHello " + username + ",\n\nThank you for joining.We’d like to confirm that your account was created successfully.If you experience any issues logging into your account, reach out to us at.\n\nRegards,\n\nThe Elearn Team"
            send_mail(
                title,
                message,
                '',
                mail_list,
                fail_silently=False,
            )
            group = Group.objects.get(name='learner')
            user.groups.add(group)
            messages.success(request, mark_safe("Registration Successful,"
                                      "<br></br>Welcome "+username))
            return redirect('loginuser')
    context={'form':form}
    return render(request,'User/registeruser.html',context)

@unauthenticated_user
def loginuser(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            messages.info(request,'Username OR Password is Incorrect')
    form = AuthenticationForm()
    context = {"form": form}
    return render(request,"User/loginuser.html",context )


def logoutuser(request):
    logout(request)
    return redirect('loginuser')

@login_required(login_url='loginuser')
@allowed_users(allowed_roles=['learner','admin'])
def index(request):
    course = Courses.objects.all()
    learner = Group.objects.get(name="learner").user_set.all().count()
    instructor = Group.objects.get(name="instructor").user_set.all().count()
    context = {"course": course, "learner": learner, "instructor": instructor}
    return render(request,'User/index.html',context)

def courses(request):
    course=Courses.objects.all()
    context = {"course":course}
    return render(request,'courses.html',context)

@login_required(login_url='loginuser')
@allowed_users(allowed_roles=['learner','admin'])
def coursesus(request):
    course=Courses.objects.all()
    context = {"course":course}
    return render(request,'User/coursesus.html',context)

def contact(request):
    return render(request,'contact.html')

@login_required(login_url='loginuser')
@allowed_users(allowed_roles=['learner','admin'])
def contactus(request):
    return render(request,'User/contactus.html')

@unauthenticated_instuser
def logininst(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('maininst')
        else:
            messages.info(request,'Username OR Password is Incorrect')
    form = AuthenticationForm()
    context = {"form": form}
    return render(request,'Instructor/logininst.html',context)

def logoutinst(request):
    logout(request)
    return redirect('logininst')

@login_required(login_url='logininst')
@allowed_users(allowed_roles=['instructor','admin'])
def maininst(request):
    inst= request.user
    course = Courses.objects.filter(author_id= inst)
    context = {"course": course}
    return render(request,'Instructor/maininst.html',context)

@login_required(login_url='loginuser')
@allowed_users(allowed_roles=['learner','admin'])
def tutorial(request,slug):
    course=Courses.objects.get(slug=slug)
    quiz=QuesModel.objects.filter(course=course)
    tutorial=Tutorialmodel.objects.filter(course=course)
    context={"tutorial": tutorial,"quiz": quiz}
    return render(request,"User/tutorial.html",context)

@login_required(login_url='loginuser')
@allowed_users(allowed_roles=['learner','admin'])
def quizes(request):
    course = Courses.objects.all()
    context = {"course": course}
    return render(request,'User/quizes.html',context)

@login_required(login_url='loginuser')
@allowed_users(allowed_roles=['learner','admin'])
def quiz(request,slug):
    course = Courses.objects.get(slug=slug)
    quiz = QuesModel.objects.filter(course=course)
    if request.method == 'POST':
        print(quiz)
        score = 0
        wrong = 0
        correct = 0
        total = 0
        for q in quiz:
            if q.is_approved:
                total += 1
                print(request.POST.get(q.question))
                print(q.ans)
                print()
                if  q.ans == request.POST.get(q.question):
                    score += 10
                    correct += 1
                else:
                    wrong += 1
        percent = score / (total * 10) * 100
        outoff=total*10
        context = {
            'score': score,
            'time': request.POST.get('timer'),
            'correct': correct,
            'wrong': wrong,
            'percent': percent,
            'total': total,
            'outoff':outoff,
            'quiz': quiz,
            'course':course,
        }
        return render(request, 'User/result.html', context)
    else:
        context={"quiz":quiz}
        return render(request,'User/quiz.html',context=context)

@login_required(login_url='loginuser')
@allowed_users(allowed_roles=['learner','admin'])
def result(request):
    return render(request, 'User/result.html')

@login_required(login_url='logininst')
@allowed_users(allowed_roles=['instructor','admin'])
def uploadtutorial(request):
    if (request.method== 'POST'):
        form= uploadtutorialform(request.POST,request.FILES)
        if (form.is_valid()):
            form.save()
            return redirect('maininst')
    form=uploadtutorialform()
    context={'form':form}
    return render(request, 'Instructor/uploadtutorial.html',context)


@login_required(login_url='logininst')
@allowed_users(allowed_roles=['instructor','admin'])
def addquiz(request):
    if (request.method == 'POST'):
        form = addQuizform(request.POST)
        for i in range(15):
            if (form.is_valid()):
                form.save()
                return redirect('addquiz')
        return redirect('maininst')
    form = addQuizform()
    context = {'form': form}
    return render(request, 'Instructor/addquiz.html', context)

def search(request):
    if request.method=='GET':
        search=request.GET.get('search')
        course = Courses.objects.filter(Course_name__icontains=search)
        context={'course':course,'search':search}
        return render(request,'search.html',context)

