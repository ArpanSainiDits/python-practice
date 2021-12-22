from django.urls import path
from .views import registerAPIView, otpVerifyAPIView, UserLoginView, ChangePasswordView, otpVerifyAPIView2


urlpatterns = [
    path('register/', registerAPIView.as_view()),
    path('otp/', otpVerifyAPIView.as_view()),
    path('otp2/', otpVerifyAPIView2.as_view()),
    path('login/', UserLoginView.as_view(), name='login'),
    path('change_password/', ChangePasswordView.as_view(), name='change_password'),

]
