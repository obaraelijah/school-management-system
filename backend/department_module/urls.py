from django.urls import path
from .views import (CreateListDepartment, RetrieveUpdateDeleteDepartment)


urlpatterns = [
    path("departments/", CreateListDepartment.as_view(), name="create-list-departments"),
    path("departments/<str:pk>/", RetrieveUpdateDeleteDepartment.as_view(), name="retrieve-update-delete-department"),
]