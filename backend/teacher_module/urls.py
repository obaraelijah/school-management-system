from django.urls import path
from .views import (CreateListTeacher, RetrieveUpdateDeleteTeacher,
                    CreateListAssignmentView, RetrieveUpdateDeleteAssignmentView)


urlpatterns = [
    path("teachers/", CreateListTeacher.as_view(), name="create-list-teachers"),
    path("teachers/<str:pk>/", RetrieveUpdateDeleteTeacher.as_view(), name="retrieve-update-delete-teacher"),
    path("teachers/<str:pk>/assignments/", CreateListAssignmentView.as_view(), name="create-list-assignment"),
    path("teachers/<str:pk>/assignments/<str:assignment_id>/", RetrieveUpdateDeleteAssignmentView.as_view(), name="retrieve-update-delete-assignment"),
]