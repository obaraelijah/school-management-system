from django.urls import path
from .views import CreateAndListSchool, RetrieveUpdateDeleteSchool, UpdateSchoolLogo

urlpatterns = [
    path("schools/", CreateAndListSchool.as_view(), name="school-create-list"),
    path("schools/<str:pk>", RetrieveUpdateDeleteSchool.as_view(), name="school-view-update-delete"),
    path("schools/<str:pk>/school_logo", UpdateSchoolLogo.as_view(), name="school-update-logo"),
]
