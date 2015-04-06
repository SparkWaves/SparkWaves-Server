from django.conf.urls import patterns, url, include
from rest_framework.urlpatterns import format_suffix_patterns
from lessons import views

urlpatterns = patterns('',
    url(r'/(?P<lesson_id>[0-9]+)/resources/(?P<resource_id>[0-9]+)$', views.LessonResourceDetail.as_view(), name="lessonResourceDetail"),
    url(r'/(?P<lesson_id>[0-9]+)/projects/(?P<project_id>[0-9]+)$', views.LessonProjectDetail.as_view(), name="lessonProjectDetail"),
    url(r'/(?P<lesson_id>[0-9]+)/resources$', views.LessonResourceList.as_view(), name="lessonResourceList"),
    url(r'/(?P<lesson_id>[0-9]+)/projects$', views.LessonProjectList.as_view(), name="lessonProjectList"),
    url(r'/(?P<lesson_id>[0-9]+)$', views.LessonDetail.as_view(), name="lessonDetail"),
    url(r'^$', views.LessonList.as_view(), name="lessonList"),
  )

urlpatterns = format_suffix_patterns(urlpatterns)
