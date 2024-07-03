from django.db import models


class Post(models.Model):
    name = models.CharField('user name', max_length=15)
    micropost = models.CharField('tweet', max_length=140, blank=True)

    def __str__(self):
        return self.name
