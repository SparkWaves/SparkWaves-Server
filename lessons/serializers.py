from rest_framework import serializers
from lessons.models import Lesson, LessonResource, LessonProject
from django.template.defaultfilters import slugify


class LessonResourceSerializer(serializers.ModelSerializer):

    class Meta:
        model = LessonResource
        fields = ('id', 'title', 'resourceType', 'url', 'description', 'image')

class LessonProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = LessonProject
        fields = ('id', 'title', 'url', 'description', 'image')
        
class LessonSerializer(serializers.ModelSerializer):
    resources = LessonResourceSerializer(many=True, read_only=True)
    projects = LessonProjectSerializer(many=True, read_only=True)

    class Meta:
        model = Lesson
        fields = ('id', 'title', 'description', 'overview', 'resources', 'projects')
