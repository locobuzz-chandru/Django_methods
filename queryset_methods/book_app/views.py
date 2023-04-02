from django.shortcuts import render
from .models import Author, Publisher, Book, Store, Item
from django.db.models import Avg, Min, Max, Count, Sum, FloatField, F, Q


def home(request):
    # b = Book.objects.count()
    # print(b)

    # pn = Book.objects.filter(publisher__name='HSRbooks').count()
    # print(pn)

    # avg = Book.objects.aggregate(Avg('price')) # aggregate(): returns a dictionary of name-value pairs
    # print(avg.get('price__avg'))

    # mx = Book.objects.aggregate(Max('price'))
    # print(mx)

    # max_avg = Book.objects.aggregate(price_diff=Max('price', output_field=FloatField()) - Avg('price'))
    # print(max_avg)

    # The output of the annotate() clause is a QuerySet; this QuerySet can be modified using any other QuerySet
    # pubs = Publisher.objects.annotate(num_books=Count('book'))
    # print(pubs)
    # print(pubs[0].num_books)

    # above_4 = Count('book', filter=Q(book__rating__gt=4.3))
    # below_4 = Count('book', filter=Q(book__rating__lte=4.4))
    # pubs = Publisher.objects.annotate(below_4=below_4).annotate(above_4=above_4)
    # print(pubs[0].above_4)
    # print(pubs[0].below_4)

    # pubs = Publisher.objects.annotate(num_books=Count('book')).order_by('-num_books')[:1]
    # print(pubs)
    # print(pubs[0].num_books)

    # all_books = Book.objects.all()
    # print([books.name for books in all_books])

    # all_avg = Book.objects.all().aggregate(Avg('price'))
    # print(all_avg)
    # all_avg = Book.objects.aggregate(Avg('price'))
    # print(all_avg)

    # avg_price = Book.objects.aggregate(average_price=Avg('price'))  # manually specify a name for the aggregate value
    # print(avg_price)

    # avg_max_min = Book.objects.aggregate(Avg('price'), Max('price'), Min('price'))
    # print(avg_max_min)

    # Per-object summaries can be generated using the annotate() clause.
    # When an annotate() clause is specified, each object in the QuerySet will be annotated with the specified values

    # q = Book.objects.annotate(Count('authors'))
    # print(q)  # queryset
    # print(q[0].name)
    # print(q[0].authors__count)

    # q = Book.objects.annotate(num_authors=Count('authors'))
    # print(q[0].num_authors)

    # book = Book.objects.first()
    # print(book.store_set.count())

    # q = Book.objects.annotate(Count('authors'), Count('store'))
    # print(q[0].authors__count, q[0].store__count)

    # q = Book.objects.annotate(Count('authors', distinct=True), Count('store', distinct=True))
    # print(q[0].authors__count, q[0].store__count)

    # an = Store.objects.annotate(min_price=Min('books__price'), max_price=Max('books__price'))
    # print(an[0].max_price)
    # ag = Store.objects.aggregate(min_price=Min('books__price'), max_price=Max('books__price'))
    # print(ag)

    # yg_age = Store.objects.aggregate(youngest_age=Min('books__authors__age'))
    # print(yg_age)

    # print(Publisher.objects.annotate(Count('book')))

    # print(Publisher.objects.aggregate(oldest_pubdate=Min('book__pubdate')))

    # authors = Author.objects.annotate(total_pages=Sum('book__pages'))
    # print(authors[0].total_pages)

    # authors = Author.objects.aggregate(average_rating=Avg('book__rating'))
    # print(authors)

    # b = Book.objects.filter(name__startswith="P").annotate(num_authors=Count('authors'))
    # print(b[0].num_authors)

    # avg_pc = Book.objects.filter(name__startswith="P").annotate(average_price=Avg('price'))
    # print(avg_pc[0].average_price)
    # print(Book.objects.filter(name__startswith="P").aggregate(Avg('price')))

    # pg = Book.objects.annotate(num_pages=Max('pages')).filter(num_pages__gt=500)
    # print(pg)
    # print(pg[3].num_pages)

    # highly_rated = Count('book', filter=Q(book__rating__gte=4.5))
    # a = Author.objects.annotate(num_books=Count('book'), highly_rated_books=highly_rated)
    # print(a)
    # print(a[0].highly_rated_books, a[0].num_books)

    # a, b = Publisher.objects.annotate(num_books=Count('book', distinct=True)).filter(book__rating__gt=4.5)
    # print(a, a.num_books)
    # print(b, b.num_books)

    # a, b = Publisher.objects.filter(book__rating__gt=4.3).annotate(num_books=Count('book'))
    # print(a, a.num_books)
    # print(b, b.num_books)

    # a = Book.objects.annotate(num_pages=Count('pages')).order_by('pages')
    # print(a)

    # a = Author.objects.annotate(average_rating=Avg('book__rating'))
    # print(a)
    # print(a[0].average_rating)

    # a = Author.objects.values('name').annotate(average_rating=Avg('book__rating'))  # authors will be grouped by name
    # print(a)  # returns dict with author name and avg rating
    # print(a[0].get('name'), a[0].get('average_rating'))

    # If the values() clause precedes the annotate() clause, any annotations will be automatically added to the result
    # set.
    # if the values() clause is applied after the annotate() clause, you need to explicitly include the aggregate column
    # a = Author.objects.annotate(average_rating=Avg('book__rating')).values('name', 'average_rating')
    # print(a)  # values() clause only constrains the fields that are generated on output

    # items = Item.objects.order_by('name')
    # a = items.values('name').annotate(Count('name'), Max('data'))
    # print(items)  # queryset
    # print(a)  # dictionary
    # a = items.values('data').annotate(Count('id')).order_by('data')
    # print(a)

    # a = Book.objects.annotate(num_authors=Count('authors')).aggregate(Max('num_authors'))
    a = Book.objects.annotate(num_authors=Count('authors')).aggregate(Count('num_authors'))
    print(a)
    return render(request, 'school/home.html')
