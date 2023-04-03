from django.urls import path

from . import views

urlpatterns = [
    path('same', views.same_origin),
]
