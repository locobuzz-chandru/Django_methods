from django.http import HttpResponse
from django.shortcuts import render
from .models import Author, Vector, Blog, Comment
from django.db.models.functions import Chr, Concat, Left, Length, Lower, LPad, MD5, Ord, Repeat, Replace, Reverse, \
    Right, RPad, SHA1, StrIndex, Substr, Trim, Upper, Abs, Ceil, Degrees, Exp, Floor, Ln, Log, Mod, Power, Radians, \
    Round, Sign, Sqrt, Cast, Coalesce, Collate, Greatest, JSONObject
from django.db.models import CharField, Value as V, FloatField, Sum
from django.db.models import F


def function(request):
    # Text Functions----------------------------------------------------------------
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

    # author = Author.objects.annotate(name_lower=Lower("name")).get()
    # print(author.name_lower)
    #
    # author = Author.objects.annotate(name_upper=Upper("name")).get()
    # print(author.name_upper)

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

    # Math Functions------------------------------------------------------------------------

    # Vector.objects.create(x=-0.5, y=1.1)
    # vector = Vector.objects.annotate(x_abs=Abs("x"), y_abs=Abs("y")).get()
    # print(vector.x_abs, vector.y_abs)

    # vector = Vector.objects.annotate(x_ceil=Ceil("x"), y_ceil=Ceil("y")).get()
    # print(vector.x_ceil, vector.y_ceil)

    # vector = Vector.objects.annotate(x_d=Degrees("x"), y_d=Degrees("y")).get()
    # print(vector.x_d, vector.y_d)  # numeric radians to degree

    # vector = Vector.objects.annotate(x_exp=Exp("x"), y_exp=Exp("y")).get()
    # print(vector.x_exp, vector.y_exp)  # e (the natural logarithm base) raised to the power of a numeric field

    # vector = Vector.objects.annotate(x_floor=Floor("x"), y_floor=Floor("y")).get()
    # print(vector.x_floor, vector.y_floor)

    # Vector.objects.create(x=5.4, y=233.0)
    # vector = Vector.objects.annotate(x_ln=Ln("x"), y_ln=Ln("y")).get()
    # print(vector.x_ln, vector.y_ln)

    # vector = Vector.objects.annotate(log=Log("x", "y")).get()
    # print(vector.log)

    # Vector.objects.create(x=5.4, y=2.3)
    # vector = Vector.objects.annotate(mod=Mod("x", "y")).get()
    # print(vector.mod)

    # vector = Vector.objects.annotate(power=Power("x", "y"))
    # print(vector[0].power)

    # vector = Vector.objects.annotate(x_r=Radians("x"), y_r=Radians("y")).get()
    # print(vector.x_r, vector.y_r)

    # Vector.objects.create(x=5.4, y=-2.37)
    # vector = Vector.objects.annotate(x_r=Round("x"), y_r=Round("y", precision=1))
    # print(vector[1].x_r, vector[1].y_r)

    # vector = Vector.objects.annotate(x_sign=Sign("x"), y_sign=Sign("y")).get()
    # print(vector.x_sign, vector.y_sign)

    # Vector.objects.create(x=4.0, y=12.0)
    # vector = Vector.objects.annotate(x_sqrt=Sqrt("x"), y_sqrt=Sqrt("y")).get()
    # print(vector.x_sqrt, vector.y_sqrt)

    # Comparison and conversion functions--------------------------------------------------------------------

    # Author.objects.create(age=25, name="Margaret Smith")
    # author = Author.objects.annotate(age_as_float=Cast("age", output_field=FloatField()),).get()
    # print(author.age_as_float)

    # Author.objects.create(name="Margaret Smith", goes_by="Maggie")
    # author = Author.objects.annotate(screen_name=Coalesce("alias", "goes_by", "name")).get()
    # print(author.screen_name)

    # aggregated = Author.objects.aggregate(combined_age=Sum("age"), combined_age_default=Sum("age", default=0),
    #                                       combined_age_coalesce=Coalesce(Sum("age"), 0), )
    # print(aggregated)  # dictionary
    # print(aggregated["combined_age"])
    # print(aggregated["combined_age_default"])
    # print(aggregated["combined_age_coalesce"])

    # blog = Blog.objects.create(body="Greatest is the best.")
    # comment = Comment.objects.create(body="No, Least is better.", blog=blog)
    # comments = Comment.objects.annotate(last_updated=Greatest("modified", "blog__modified"))
    # annotated_comment = comments.get()
    # print(annotated_comment.last_updated)

    # comments = Comment.objects.annotate(last_updated=Greatest("modified", "blog__modified"))
    # annotated_comment = comments.get()
    # print(annotated_comment.last_updated)

    # Author.objects.create(name="Margaret Smith", alias="msmith", age=25)
    # author = Author.objects.annotate(json_object=
    #                                  JSONObject(name=Lower("name"),
    #                                             alias="alias",
    #                                             age=F("age") * 2,)).get()
    # print(author.json_object)

    return HttpResponse("database functions")
