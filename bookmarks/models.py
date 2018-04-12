from uuid import uuid4
from django.db import models

# Create your models here.
class Bookmark(models.Model):
    FILM = 'FI'
    GAME = 'GA'
    MUSIC = 'MU'
    TECH = 'TE'
    TYPE_OF_BOOKMARK_CHOICES = (
        (FILM, 'Film'),
        (GAME, 'Gaming'),
        (MUSIC, 'Music'),
        (TECH, 'Tech'),
    )
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField('Name', max_length=200)
    notes = models.TextField('Notes', blank=True)
    url = models.URLField('URL', unique=True)
    category = models.CharField(
        'Category',
        max_length=50,
        choices=TYPE_OF_BOOKMARK_CHOICES,
        blank=True,
        null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Bookmark'
        verbose_name_plural = 'Bookmarks'

    def __unicode__(self):
        return self.name