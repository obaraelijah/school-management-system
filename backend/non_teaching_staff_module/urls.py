from django.urls import path
from .views import (CreateListNonTeachingStaffView, RetrieveUpdateDestroyNonTeachingStaffView)


urlpatterns = [
    path("non-teaching-staff/", CreateListNonTeachingStaffView.as_view(), name="create-list-non-teaching-staff"),
    path("non-teaching-staff/<str:pk>/", RetrieveUpdateDestroyNonTeachingStaffView.as_view(), name="retrieve-update-destroy-non-teaching-staff"),
]