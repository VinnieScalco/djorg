from django.db import models

# Create your models here.
class bookmarks(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=1000)
    url = models.URLField()

    class Meta:
        unique_together = (("user", "name"),("url", "user") )
    
    def __unicode__(self):
        return self.url
