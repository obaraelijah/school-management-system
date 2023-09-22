from django.urls import path
from .views import (CreateListCourse, RetrieveUpdateDeleteCourse)


urlpatterns = [
    path("courses/", CreateListCourse.as_view(), name="create-list-courses"),
    path("courses/<str:pk>/", RetrieveUpdateDeleteCourse.as_view(), name="retrieve-update-delete-course"),
]