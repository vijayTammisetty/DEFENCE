from operator import imod
from django.urls import path
from . import views

urlpatterns = [
    path('',views.main_dashbord, name='home'),
    path('about/',views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]
