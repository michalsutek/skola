from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('studenti/', views.list_students, name="list-students"),
    path('ucitelia/', views.list_teachers, name="list-teachers"),
    path('triedy/', views.list_triedy, name="list-class"),
]
