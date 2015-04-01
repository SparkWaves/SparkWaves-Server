from django.db import models

class Profile(models.Model):
    email = models.EmailField(unique=True)
    createdDate = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.email
