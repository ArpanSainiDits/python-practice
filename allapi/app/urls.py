from django.urls import path
from .views import registerAPIView, otpVerifyAPIView, UserLoginView, forgetPasswordView, otpVerifyView2


urlpatterns = [
    path('register/', registerAPIView.as_view()),
    path('otpRegister/', otpVerifyAPIView.as_view()),
    path('login/', UserLoginView.as_view()),
    path('forgotPassword/', forgetPasswordView.as_view()),
    path('otpForgotPassword/', otpVerifyView2.as_view()),
    
    
]