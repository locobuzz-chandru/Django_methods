from django.contrib import admin
from django.urls import path, include
# from student import views
from book_app import views
# from database_functions import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('query/', views.home),
    # path('same/', views.same_origin),
    # path('', views.function),
]
