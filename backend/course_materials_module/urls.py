from django.urls import path
from .views import (CreateListCourseMaterialView, RetrieveUpdateDestroyCourseMaterialView)


urlpatterns = [
    path("course-materials/", CreateListCourseMaterialView.as_view(), name="create-list-course-material"),
    path("course-materials/<str:pk>/", RetrieveUpdateDestroyCourseMaterialView.as_view(), name="retrieve-update-destroy-course-material"),
]