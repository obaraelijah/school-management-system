from django.urls import path
from .views import CreateListRoles, RetrieveUpdateRole, CreateRetrieveUsers, RetrieveUpdateDeleteUser


urlpatterns = [
    path("roles", CreateListRoles.as_view(), name="create-list-Roles"),
    path("roles/<str:pk>", RetrieveUpdateRole.as_view(), name="retrieve-update-Role"),
    path("users", CreateRetrieveUsers.as_view(), name="create-list-Users"),
    path("users/<str:pk>", RetrieveUpdateDeleteUser.as_view(), name="retrive-update-delete-User")
]