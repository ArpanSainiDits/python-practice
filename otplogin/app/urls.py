from django.urls import path
from .views import registerAPIView


urlpatterns = [
    path('register/', registerAPIView.as_view()),
 

]
