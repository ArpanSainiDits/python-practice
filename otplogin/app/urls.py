from django.urls import path
from .views import registerAPIView, otpVerifyAPIView, UserLoginView


urlpatterns = [
    path('register/', registerAPIView.as_view()),
    path('otp/', otpVerifyAPIView.as_view()),
    path('login/', UserLoginView.as_view(), name='login'),

]
