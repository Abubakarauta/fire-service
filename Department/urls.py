from .views import *
from django.urls import path

urlpatterns =  [
    path('',index , name='index'),
    path('about/', about , name='about'),
    path('contact/',contact, name='contact'),
    path('departments/',department,name='department'),
    path('<int:id>/department_detail', department_detail, name="department_detail"),
    path("gallery/", gallery, name="gallery"),
    path('members/',members, name='members'),
    path('news/',news,name='news'),
    path("survival/", survival_view, name="survival"),
    path('staff/',staff , name='staff'),


]