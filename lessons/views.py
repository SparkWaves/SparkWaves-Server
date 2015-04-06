from lessons.models import Lesson, LessonResource, LessonProject
from lessons.serializers import LessonResourceSerializer, LessonProjectSerializer, LessonSerializer
from lessons.permissions import IsStaffOrReadOnly
from rest_framework import generics
from django.shortcuts import get_object_or_404
from django.template.defaultfilters import slugify



class LessonList(generics.ListCreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = (IsStaffOrReadOnly,)

class LessonDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = LessonSerializer
    permission_classes = (IsStaffOrReadOnly,)

    def get_object(self):
        lesson_id = self.kwargs['lesson_id']
        lesson = get_object_or_404(Lesson, id=lesson_id)
        self.check_object_permissions(self.request, lesson)
        return lesson

class LessonResourceList(generics.ListCreateAPIView):
    serializer_class = LessonResourceSerializer
    permission_classes = (IsStaffOrReadOnly,)

    def perform_create(self, serializer):
        lesson_id = self.kwargs['lesson_id']
        lesson = get_object_or_404(Lesson, id=lesson_id)
        serializer.save(lesson=lesson)

    def get_queryset(self):
        lesson_id = self.kwargs['lesson_id']
        return LessonResource.objects.filter(lesson__id=lesson_id)

class LessonResourceDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = LessonResourceSerializer
    permission_classes = (IsStaffOrReadOnly,)

    def get_object(self):
        lesson_id = self.kwargs['lesson_id']
        resource_id = self.kwargs['resource_id']
        resource = get_object_or_404(LessonResource, id=resource_id, lesson__id=lesson_id)
        self.check_object_permissions(self.request, resource)
        return resource

class LessonProjectList(generics.ListCreateAPIView):
    serializer_class = LessonProjectSerializer
    permission_classes = (IsStaffOrReadOnly,)

    def perform_create(self, serializer):
        lesson_id = self.kwargs['lesson_id']
        lesson = get_object_or_404(Lesson, id=lesson_id)
        serializer.save(lesson=lesson)

    def get_queryset(self):
        lesson_id = self.kwargs['lesson_id']
        return LessonProject.objects.filter(lesson__id=lesson_id)

class LessonProjectDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = LessonProjectSerializer
    permission_classes = (IsStaffOrReadOnly,)

    def get_object(self):
        lesson_id = self.kwargs['lesson_id']
        project_id = self.kwargs['project_id']
        project = get_object_or_404(LessonProject, id=project_id, lesson__id=lesson_id)
        self.check_object_permissions(self.request, project)
        return project
