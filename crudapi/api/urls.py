from django.urls import path
from api import views



urlpatterns = [
    path('stucreate/',views.student_create),
]
