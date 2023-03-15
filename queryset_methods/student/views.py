from django.shortcuts import render
from .models import Student, Teacher
from django.db.models import Q


def home(request):
    # student_data = Student.objects.all()
    # student_data = Student.objects.filter(marks=55)
    # student_data = Student.objects.exclude(marks=55)

    # student_data = Student.objects.order_by('marks')
    # student_data = Student.objects.order_by('-marks')
    # student_data = Student.objects.order_by('?')
    # student_data = Student.objects.order_by('id').reverse()[:5]

    # student_data = Student.objects.values()  # queryset that returns dictionaries, each represent an object
    # student_data = Student.objects.values('name', 'city')

    # student_data = Student.objects.values_list()  # similar to values(), returns tuple
    # student_data = Student.objects.values_list('name', 'city')
    # student_data = Student.objects.values_list('name', 'city', named=True)

    # student_data = Student.objects.using('default')
    # student_data = Student.objects.dates('pass_date', 'month', 'DESC')

    # UNION
    # q1 = Student.objects.values_list('id', 'name', named=True)
    # q2 = Teacher.objects.values_list('id', 'name', named=True)
    # student_data = q2.union(q1, all=True)

    # INTERSECTION
    # q1 = Student.objects.values_list('id', 'name', named=True)
    # q2 = Teacher.objects.values_list('id', 'name', named=True)
    # student_data = q2.intersection(q1)  # returns shared elements of 2/more querysets

    # DIFFERENCE
    # q1 = Student.objects.values_list('id', 'name', named=True)
    # q2 = Teacher.objects.values_list('id', 'name', named=True)
    # student_data = q1.difference(q2)  # uses EXCEPT operator to keep only elements present in QuerySet but not in some
    # other QuerySet

    # AND
    # student_data = Student.objects.filter(id=1) & Student.objects.filter(roll=10)
    # student_data = Student.objects.filter(id=1, roll=10)
    # student_data = Student.objects.filter(Q(id=1) & Q(roll=10))

    # OR
    # student_data = Student.objects.filter(id=1) | Student.objects.filter(roll=12)
    # student_data = Student.objects.filter(Q(id=1) | Q(roll=12))

    # student_data = (Student.objects.filter(city='Bangalore') | Student.objects.filter(marks=70)).distinct()

    # student_data = Student.objects.get(id=1)
    # student_data = Student.objects.first()
    # student_data = Student.objects.order_by('marks').first()

    # student_data = Student.objects.last()

    # student_data = Student.objects.latest('pass_date')
    # student_data = Student.objects.earliest('pass_date')

    # student_data = Student.objects.filter(id=11).exists()

    # student_data = Student.objects.create(name='Sam', roll=28, city='Mumbai', marks=60, pass_date='2023-3-15')

    # student_data, created = Student.objects.get_or_create(name='Sam', roll=28, city='Mumbai', marks=60,
    #                                                       pass_date='2023-3-15')
    # print(student_data, created)  # created returns False if data is already exists

    # student_data = Student.objects.filter(id=1).update(marks=96)  # update with get gives error

    # student_data, created = Student.objects.update_or_create(id=2, name='Ajay', defaults={'name': 'Chiru'})

    objs = [
        Student(name='Ganga', roll=41, city='Ranchi', marks=70, pass_date='2023-3-2'),
        Student(name='Raina', roll=29, city='Koli', marks=32, pass_date='2023-2-25'),
        Student(name='Shami', roll=52, city='Dhaka', marks=86, pass_date='2023-1-4'),
    ]
    # student_data = Student.objects.bulk_create(objs)

    # all_student_data = Student.objects.filter(marks=70)
    # for student in all_student_data:
    #     student.city = 'Bangalore'
    # student_data = Student.objects.bulk_update(all_student_data, ['city'])

    # student_data = Student.objects.in_bulk([1, 2])
    # print(student_data[1].name)  # Chandru
    # student_data = Student.objects.in_bulk([])
    # student_data = Student.objects.in_bulk() #  returns all objects with key value pair(id as key)

    # student_data = Student.objects.get(id=6).delete()
    student_data = Student.objects.all().count()

    print(student_data)
    # print('SQL query': student_data.query)
    return render(request, 'school/home.html', {'student': student_data})
    # QuerySet is a collection of data from a database
