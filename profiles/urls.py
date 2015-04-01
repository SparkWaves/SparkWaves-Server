from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from profiles import views

urlpatterns = patterns('',
    url(r'^$', views.ProfileList.as_view(), name="ProfileList"),
)

urlpatterns = format_suffix_patterns(urlpatterns)
