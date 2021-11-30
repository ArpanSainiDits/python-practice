
from django.views.generic import TemplateView
# from myapp import views
from django.urls import path
from . import views

urlpatterns = [

    path('login/', views.login),
]
