from django.urls import path
from .views import CreateAndListSchool, RetrieveUpdateDeleteSchool, UpdateSchoolLogo

urlpatterns = [
    path("", CreateAndListSchool.as_view(), name="school-create-list"),
    path("/<str:pk>", RetrieveUpdateDeleteSchool.as_view(), name="school-view-update-delete"),
    path("/<str:pk>/school_logo", UpdateSchoolLogo.as_view(), name="school-update-logo"),
]
