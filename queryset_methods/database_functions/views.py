from django.http import HttpResponse
from django.shortcuts import render
from .models import Author
from django.db.models.functions import Chr, Concat, Left, Length, Lower, LPad, MD5, Ord, Repeat, Replace, Reverse, \
    Right, RPad, SHA1, StrIndex, Substr, Trim, Upper
from django.db.models import CharField, Value as V


def function(request):
    # Author.objects.create(name="Margaret Smith")
    # author = Author.objects.filter(name__startswith=Chr(ord("M"))).get()
    # print(author.name)

    # Author.objects.create(goes_by="Maggie")
    # author = Author.objects.annotate(
    #     screen_name=Concat("name", V(" ("), "goes_by", V(")"), output_field=CharField())).get()
    # print(author.screen_name)

    # author = Author.objects.annotate(first_initial=Left("name", 1)).get()
    # print(author.first_initial)

    # author = Author.objects.annotate(name_length=Length("name"), goes_by_length=Length("goes_by")).get()
    # print(author.name_length, author.goes_by_length)

    author = Author.objects.annotate(name_lower=Lower("name")).get()
    print(author.name_lower)

    author = Author.objects.annotate(name_upper=Upper("name")).get()
    print(author.name_upper)

    # Author.objects.create(name="John", alias="j")
    # Author.objects.update(name=LPad("name", 8, V("abc")))
    # Author.objects.update(name=RPad("name", 8, V("abc")))
    # print(Author.objects.get(alias="j").name)

    # Author.objects.create(name="Margaret Smith")
    # author = Author.objects.annotate(name_md5=MD5("name")).get()
    # print(author.name_md5)

    # author = Author.objects.annotate(name_code_point=Ord("name")).get()
    # print(author.name_code_point)

    # Author.objects.create(name="John", alias="j")
    # Author.objects.update(name=Repeat("name", 3))
    # print(Author.objects.get(alias="j").name)

    # Author.objects.create(name="Margaret Johnson")
    # Author.objects.create(name="Margaret Smith")
    # Author.objects.update(name=Replace("name", V("Margaret"), V("Margareth")))
    # print(Author.objects.values("name"))

    # author = Author.objects.annotate(backward=Reverse("name")).get()
    # print(author.backward)

    # author = Author.objects.annotate(last_letter=Right("name", 4)).get()
    # print(author.last_letter)

    # Author.objects.create(name="Margaret Smith")
    # author = Author.objects.annotate(name_sha1=SHA1("name")).get()
    # print(author.name_sha1)

    # author = Author.objects.filter(name="Margareth Smith").annotate(smith_index=StrIndex("name", V("Smith"))).get()
    # print(author.smith_index)  # 11

    # authors = Author.objects.annotate(smith_index=StrIndex("name",V("Smith"))).filter(smith_index__gt=0)
    # print(authors)

    # Author.objects.update(alias=Lower(Substr("name", 1, 5)))
    # print(Author.objects.get(name="Margareth Smith").alias)  # marga

    # Author.objects.create(name="  John  ", alias="j")
    # Author.objects.update(name=Trim("name"))
    # print(Author.objects.get(alias="j").name)

    return HttpResponse("database functions")
