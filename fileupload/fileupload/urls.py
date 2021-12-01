
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from file import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('profileById/<int:id>/', views.profileView1.as_view()),
    path('profile/', views.profileView.as_view()),
]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
