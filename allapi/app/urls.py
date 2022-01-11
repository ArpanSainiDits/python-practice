from django.urls import path
from .views import registerAPIView, otpVerifyAPIView, UserLoginView, forgetPasswordView, otpVerifyView2, changePasswordView, taskView, taskViewById, userProfileView


urlpatterns = [
    path('register/', registerAPIView.as_view()),
    path('otpRegister/', otpVerifyAPIView.as_view()),
    path('login/', UserLoginView.as_view()),
    path('forgotPassword/', forgetPasswordView.as_view()),
    path('otpForgotPassword/', otpVerifyView2.as_view()),
    path('changePassword/', changePasswordView.as_view()),
    path('task/', taskView.as_view()),
    path('taskById/<int:id>/', taskViewById.as_view()),
    path('userProfileView/<int:id>/', userProfileView.as_view()),
    
    
]