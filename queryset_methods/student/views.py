from django.shortcuts import render
from .models import Student, Teacher
from django.db.models import Q
from datetime import date, time


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
    # student_data = Student.objects.dates('passdate', 'month', 'DESC')

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

    # student_data = Student.objects.get(id=17)
    # student_data = Student.objects.first()
    # student_data = Student.objects.order_by('marks').first()

    # student_data = Student.objects.last()

    # student_data = Student.objects.latest('passdate')
    # student_data = Student.objects.earliest('passdate')

    # student_data = Student.objects.filter(id=11).exists()

    # student_data = Student.objects.create(name='Sam', roll=28, city='Mumbai', marks=60, passdate='2023-3-15')

    # student_data, created = Student.objects.get_or_create(name='Sam', roll=28, city='Mumbai', marks=60,
    #                                                       passdate='2023-3-15')
    # print(student_data, created)  # created returns False if data is already exists

    # student_data = Student.objects.filter(id=1).update(marks=96)  # update with get gives error

    # student_data, created = Student.objects.update_or_create(id=2, name='Ajay', defaults={'name': 'Chiru'})

    objs = [
        Student(name='Ganga', roll=41, city='Ranchi', marks=70, passdate='2023-3-2'),
        Student(name='Raina', roll=29, city='Koli', marks=32, passdate='2023-2-25'),
        Student(name='Shami', roll=52, city='Dhaka', marks=86, passdate='2023-1-4'),
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
    # student_data = Student.objects.all().count()

    # FIELD LOOKUPS ======================================================
    # student_data = Student.objects.filter(name__exact='Nik') # # case-sensitive
    # student_data = Student.objects.filter(name__iexact='nik') # case-insensitive

    # student_data = Student.objects.filter(name__contains='A') # case-sensitive
    # student_data = Student.objects.filter(name__icontains='A') # case-insensitive

    # student_data = Student.objects.filter(id__in=[4, 5, 17])
    # student_data = Student.objects.filter(marks__in=[55, 60])

    # student_data = Student.objects.filter(marks__gt=70).count()
    # student_data = Student.objects.filter(marks__gte=70).count()

    # student_data = Student.objects.filter(marks__lt=70)
    # student_data = Student.objects.filter(marks__lte=70)

    student_data = Student.objects.get(name__startswith='J')
    # student_data = Student.objects.filter(name__istartswith='a')

    # student_data = Student.objects.filter(name__endswith='y')
    # student_data = Student.objects.filter(marks__endswith=0)

    # student_data = Student.objects.filter(marks__range=(30, 58))

    # student_data = Student.objects.filter(admdatetime__date=date(2023, 3, 16))
    # student_data = Student.objects.filter(admdatetime__date__gt=date(2022, 1, 1)).count()

    # student_data = Student.objects.filter(passdate__year=2020)
    # student_data = Student.objects.filter(passdate__year__lt=2023)

    # student_data = Student.objects.filter(passdate__month=2)
    # student_data = Student.objects.filter(passdate__month__gt=1).count()

    # student_data = Student.objects.filter(passdate__day=15)
    # student_data = Student.objects.filter(passdate__day__gt=15)

    # student_data = Student.objects.filter(passdate__week=10)

    # student_data = Student.objects.filter(passdate__week_day=5)

    # student_data = Student.objects.filter(passdate__quarter=1)

    # student_data = Student.objects.filter(admdatetime__time=time(6, 00))

    # student_data = Student.objects.filter(admdatetime__second=0)
    # student_data = Student.objects.filter(admdatetime__second__gt=0).count()

    # student_data = Student.objects.filter(roll__isnull=False)

    # student_data = Student.objects.get(name__exact='Nik')

    # student_data = Student.objects.filter(name__regex=r'^(Ni?|Cha+)+')
    # student_data = Student.objects.filter(name__iregex=r'^(ni?|cha+)+')

    print(student_data)
    # print('SQL query': student_data.query)
    return render(request, 'school/home.html', {'student': student_data})
    # QuerySet is a collection of data from a database
    # Field lookups are how we specify the meat of an SQL WHERE clause. They’re specified as keyword arguments to the
    # QuerySet methods filter(), exclude() and get()
