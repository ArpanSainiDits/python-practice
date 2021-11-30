
from django.urls import path, include
from rest_framework import routers
from .views import student_detail, student_detail1, student_list, student_list1, StudentAPIView, StudentDetailAPIView, GenericAPIView, StudentViewSet, StudentGenericViewSet, StudentModelViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('student', StudentViewSet, basename='student')

router2 = DefaultRouter()
router2.register('student', StudentGenericViewSet, basename= 'student')

router3 = DefaultRouter()
router3.register('student', StudentModelViewSet, basename='student')


urlpatterns = [
    path('modelviewset/', include(router3.urls)),
    path('modelviewset/<int:pk>/', include(router3.urls)),
    
    path('genericviewset/', include(router2.urls)),
    path('genericviewset/<int:pk>/', include(router2.urls)),
    
    path('viewset/',include(router.urls)),
    path('viewset/<int:pk>/', include(router.urls)),

    path('student/', student_list),
    path('student1/', student_list1),
    path('studentId/<int:pk>/', student_detail),
    path('studentId1/<int:pk>/', student_detail1),
    path('studentClass/', StudentAPIView.as_view()),
    path('studentClassId/<int:id>/', StudentDetailAPIView.as_view()),
    path('GenericAPIView/<int:id>/', GenericAPIView.as_view()),
    path('GenericAPIView/', GenericAPIView.as_view())


]
 