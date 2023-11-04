from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path, include  # Import the 'include' function

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),  # Include your application's URLs
]

urlpatterns = [
    path('students/', views.students_view, name='students'),
    path('courses/', views.courses_view, name='courses'),
    path('details/<int:student_id>/', views.details_view, name='details'),
]

