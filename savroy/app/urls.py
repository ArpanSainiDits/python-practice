from django.urls import path, include
from .views import *
urlpatterns = [

    path('about/', about, name = 'about'),
    path('components/', components, name= 'components'),
    path('contact/', contact, name = 'contact' ),
    path('index/', index, name='index'),
    path('project/', project, name = 'project'),
    path('sample/', sample , name= 'sample'),
    path('services/', services, name='services'),

]
