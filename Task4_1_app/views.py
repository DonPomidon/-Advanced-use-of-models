from django.shortcuts import render
from .models import Teacher, ClassDetails, Student, AdultStudent, YoungStudent


def home(request):
    return render(request, 'home.html', {'home': home})


def teacher(request):
    teachers = Teacher.objects.all()
    return render(request, 'teachers.html', {'teachers': teachers})


def class_detail(request):
    class_details = ClassDetails.objects.all()
    return render(request, 'class_details.html', {'class_details': class_details})


def student(request):
    students = Student.objects.all()
    return render(request, 'students.html', {'students': students})


def adult_student(request):
    adult_students = AdultStudent.object.all()
    return render(request, 'adult_students.html', {'adult_students': adult_students})


def young_student(request):
    young_students = YoungStudent.object.all()
    return render(request, 'young_students.html', {'young_students': young_students})

