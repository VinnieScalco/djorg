from uuid import uuid4
from django.db import models

# Create your models here.
class Bookmark(models.Model):
    FILM = 'Fi'
    MUSIC = 'Mu'
    TECH = 'Te'
    GAME = 'Ga'
    TYPE_OF_BOOKMARK_CHOICES = (
        (FILM, 'Film'),
        (MUSIC, 'Music'),
        (TECH, 'Tech'),
        (GAME, 'Gaming')
    )
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField('Name', max_length=200)
    notes = models.TextField('Notes', blank=True)
    url = models.URLField('URL', unique=True)
    category = models.CharField('Category', blank=True, null=True, max_length=100)
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