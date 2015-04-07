from django.db import models

class Lesson(models.Model):
    title = models.CharField(max_length=100)
    overview = models.CharField(max_length=10000, blank=True, null=True)
    image = models.URLField(blank=True, null=True)

    def __unicode__(self):
        return self.title

class LessonResource(models.Model):
    lesson = models.ForeignKey(Lesson, related_name='resources')
    title = models.CharField(max_length=100)
    resourceType = models.CharField(max_length=100)
    url = models.URLField()
    description = models.CharField(max_length=1000, blank=True, null=True)
    image = models.URLField(blank=True, null=True)

    def __unicode__(self):
        return self.title

class LessonProject(models.Model):
    lesson = models.ForeignKey(Lesson, related_name='projects')
    title = models.CharField(max_length=100)
    url = models.URLField()
    description = models.CharField(max_length=1000, blank=True, null=True)
    image = models.URLField(blank=True, null=True)

    def __unicode__(self):
        return self.title
