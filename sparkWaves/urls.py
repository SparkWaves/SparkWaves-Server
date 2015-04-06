from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.views.generic import TemplateView


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/profiles', include('profiles.urls')),
    url(r'^api/lessons', include('lessons.urls')),
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^api/registration', include('rest_auth.registration.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
)

if settings.LIVEHOST != True:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))
