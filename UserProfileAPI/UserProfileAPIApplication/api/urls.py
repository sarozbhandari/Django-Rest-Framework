from django.urls import path
from UserProfileAPIApplication.api.views import ProfileList

urlpatterns = [
    path("profiles/", ProfileList.as_view(), name = "profile-list")
]