from rest_framework import serializers
from profiles.models import Profile

class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ('id', 'email', 'createdDate')

    def validate_email(self, attrs):
        """
        Check that the tool name does not already exist
        """

        email = attrs
        profiles = Profile.objects.filter(email__iexact=email)
        if len(profiles) != 0:
            raise serializers.ValidationError("This email address is already registered.")
        return attrs
