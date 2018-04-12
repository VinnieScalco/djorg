from uuid import uuid4
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Bookmark(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField('Name', max_length=200)
    notes = models.TextField('Notes', blank=True)
    url = models.URLField('URL', unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Bookmark'
        verbose_name_plural = 'Bookmarks'

    def __unicode__(self):
        return self.name

# class FilmBookmark(Bookmark):
#         name = models.CharField(max_length=200)
#         notes = models.TextField('Notes', blank=True)
#         url = models.URLField('URL', unique=True)
#         created_at = models.DateTimeField(auto_now_add=True)
#         last_modified = models.DateTimeField(auto_now=True)

# class GameBookmark(Bookmark):
#         name = models.CharField(max_length=200)
#         notes = models.TextField('Notes', blank=True)
#         url = models.URLField('URL', unique=True)
#         created_at = models.DateTimeField(auto_now_add=True)
#         last_modified = models.DateTimeField(auto_now=True)