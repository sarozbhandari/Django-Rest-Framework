from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from UserProfileAPIApplication.models import Profile
from UserProfileAPIApplication.api.serializers import ProfileSerializer

class ProfileList(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]