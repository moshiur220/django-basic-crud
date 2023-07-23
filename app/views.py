from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Student
# Create your views here.


def show_students(request):
    students = Student.objects.all()
    return render(request, 'show_students.html', {'students': students})


def add_student(request):
    if request.method == 'POST':
        # Get the form data submitted by the user
        stname = request.POST['stname']
        stemail = request.POST['stemail']
        stdep = request.POST['stdep']

        # Create and save the Student object to the database
        student = Student(stname=stname, stemail=stemail, stdep=stdep)
        student.save()

        # Redirect to a success page or any other desired view
        # return redirect('success')

    return render(request, 'add_student.html')


def show_student_by_id(request, student_id):
    student = get_object_or_404(Student, id=student_id)

    print(student)
    print("Here is the student")
    return render(request, 'show_student_by_id.html', {'student': student})


def update_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)

    if request.method == 'POST':
        # Get the updated form data submitted by the user
        stname = request.POST['stname']
        stemail = request.POST['stemail']
        stdep = request.POST['stdep']

        # Update the Student object with the new data
        student.stname = stname
        student.stemail = stemail
        student.stdep = stdep
        student.save()

        # Redirect to a success page or any other desired view
        return redirect('student_detail', student_id=student_id)

    return render(request, 'update_student.html', {'student': student})
