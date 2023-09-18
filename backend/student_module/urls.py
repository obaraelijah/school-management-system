from django.urls import path
from .views import (CreateListStudentView, RetrieveUpdateDestroyStudentView)


urlpatterns = [
    path("students/", CreateListStudentView.as_view(), name="create-list-student"),
    path("students/<str:pk>/", RetrieveUpdateDestroyStudentView.as_view(), name="retrieve-update-destroy-student"),
]