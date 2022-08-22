from pprint import pprint

from django.shortcuts import render, redirect
from django.urls import reverse

from . import models


# Create your views here.
def index_page(request):
    print("Request received")
    pprint(request)
    favorite_courses = models.Course.objects.all()[:10]
    favorite_students = models.Student.objects.select_related('course').all()[:5]
    for student in favorite_students:
        print(student.date_of_birth, student.course.name)

    context = {
        "username": "Some User",
        "favorite_courses": favorite_courses,
        "favorite_students": favorite_students
    }
    return render(request, "main/index.html", context)


def login_page(request):
    return render(request, "main/login.html", {})


def courses_page(request):
    all_courses = models.Course.objects.all()
    return render(request, "main/courses.html", {"all_courses": all_courses})


def results_page(request):
    print(request)
    print(request.GET)
    if request.method == "GET":
        search_pattern = request.GET.get("course_name", None)
        if search_pattern:
            all_courses = models.Course.objects.filter(name__icontains=search_pattern[0])
        else:
            all_courses = models.Course.objects.all()

        return render(request, "main/courses.html", {"all_courses": all_courses})

    return render(request, "main/courses.html", {})


def course_detail_page(request, pk):
    print("Primary key:", pk)
    course = models.Course.objects.get(pk=pk)
    comments = models.Comment.objects.filter(course=course)
    if request.method == "GET":
        return render(request, "main/course_detail_page.html", {"course": course, "comments": comments})
    else:
        author = request.POST.get("author", None)
        text = request.POST.get("comment", None)
        course = models.Course.objects.get(pk=pk)
        models.Comment.objects.create(
            author=author,
            comment_text=text,
            course=course
        )
        return redirect(reverse("main:course_detail_page", args=(pk,)))
