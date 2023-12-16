from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from home.models import Contact, Teacher_details
from django.contrib import messages
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.models import User
from .forms import TeacherForm
import os
from django.conf import settings


def homepage(request):
    print(request.user)
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request, 'index.html')


def aboutus(request):
    return render(request, "aboutus.html")


def inner_login(request):
    return render(request, "inner_login.html")


def super_user(request):
    results = Teacher_details.objects.all()
    return render(request, 'super_user.html', {'results': results})

# def show_more(request):
#     return render(request, 'show_more.html')


def show_more(request,id):
    # query = request.GET.get('q')
    results = Teacher_details.objects.filter(tid=id)
    return render(request, 'show_more.html', {'results': results})


def edit(request, pk):
    teacher = Teacher_details.objects.get(pk=pk)
    return render(request, 'edit_teacher.html', {'teacher': teacher})


def update(request, pk):
    teacher = Teacher_details.objects.get(pk=pk)
    form = TeacherForm(request.POST, instance=teacher)
    if form.is_valpk():
        form.save()
        return redirect("/super_user")

    return render(request, 'edit_teacher.html', {'teacher': teacher})


def destroy(request, pk):
    teacher = Teacher_details.objects.get(pk=pk)
    teacher.delete()
    return redirect("/super_user")


# ----------------------------------------------------------Add New Teacher----------------------------------------------

def teacherform(request):
    if request.method == "POST":
        tname = request.POST.get('tname')
        temail = request.POST.get('temail')
        tphone = request.POST.get('tphone')
        tdob = request.POST.get('tdob')
        tadd = request.POST.get('tadd')
        # eduactional details
        tsscp = request.POST.get('tsscp')
        thscs = request.POST.get('thscs')
        thscp = request.POST.get('thscp')
        tgp = request.POST.get('tgp')
        tgc = request.POST.get('tgc')
        tpgp = request.POST.get('tpgp')
        tpgc = request.POST.get('tpgc')
        # Professional Details
        tge = request.POST.get('tge')
        teq = request.POST.get('teq')
        teqy = request.POST.get('teqy')
        teacher_service = request.POST.get('teacher_service')
        join_date = request.POST.get('join_date')
        teacher_salary = request.POST.get('teacher_salary')
        teacher_exp = request.POST.get('teacher_exp')
        field_name = request.POST.get('upload_file')
        Tdetails = Teacher_details(tname=tname, temail=temail, tphone=tphone, tdob=tdob, tadd=tadd, tsscp=tsscp, thscs=thscs, thscp=thscp, tgp=tgp, tgc=tgc, tpgp=tpgp, tpgc=tpgc,
                                   tge=tge, teq=teq, teqy=teqy, teacher_service=teacher_service, join_date=join_date, teacher_salary=teacher_salary, teacher_exp=teacher_exp, field_name=field_name)

        Tdetails.save()
        messages.success(request, 'Your Profile Saved Successfully !.')
    else:
        return render(request, "teacherform.html")

    return render(request, "teacherform.html")
# -----------------------------------------------------list Teacher---------------------------------------------------


def contactus(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, desc=desc)
        contact.save()
        messages.success(request, 'Thank You For Contacting Us !.')
    else:
        return render(request, "contactus.html")

    return render(request, "contactus.html")


def registrationuser(request):
    if request.method == "POST":
        username = request.POST.get('user')
        email = request.POST.get('email')
        password = request.POST.get('pass')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        user = User.objects.create_user(username, email, password)
        user.first_name = fname
        user.last_name = lname
        user.save()
        return redirect('login')
        messages.success(request, 'You Sign Up Successfully !.')

    else:
        return render(request, 'Registration_Form.html')


def loginUser(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)

        # check if user has entered correct credentials
        user = authenticate(username=username, password=password)

        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            return redirect("/")
            messages.success(request, 'You Sign In Successful')
        else:
            # No backend authenticated the credentials
            return render(request, 'login.html')
            messages.warning(request, 'Wrong Credentials !')

    return render(request, 'login.html')


def logoutUser(request):
    logout(request)
    return redirect("/login")
