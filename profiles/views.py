from profiles.models import Profile
from profiles.serializers import ProfileSerializer
from profiles.permissions import IsAdminOrWriteOnly
from rest_framework import generics, permissions, filters

class ProfileList(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (permissions.AllowAny, IsAdminOrWriteOnly,)
