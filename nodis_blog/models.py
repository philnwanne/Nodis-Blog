from typing import Text
from django.db import models
from django.db.models.fields import CharField, SlugField, TextField
from django.contrib.auth.models import User


STATUS = (
    (0,"Draft"),
    (1,"Publish"),
    (2, "Delete")
)
# Create your models here.

'''# Profile Model/Class
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.PROTECT,)
    website = models.URLField(blank=True)
    bio = models.CharField(max_length=500, blank=True)
'''

# Tag Model/Class
class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)


# Post Model/Class
class Post(models.Model):
    # title field using charfield constraint with unique constraint    
    title = models.CharField(max_length=255, unique=True)
    # subtitle field using charfield constraint
    ##subtitle = models.CharField(max_length=255, blank=True)
    # slug field using charfield constraint with unique constraint
    slug = models.SlugField(max_length=255, unique=True)
    # body field to store our post
    content = models.TextField()
    # meta description for SEO benifits
    ##meta_description = models.CharField(max_length=150, blank=True)
    # and date time fields automatically populated using system time
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    ##publish_date = models.DateTimeField(blank=True, null=True)
    ##published = models.BooleanField(default=False)
    # author field populated using users database
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    tags = models.ManyToManyField(Tag, blank=True)
    status = models.IntegerField(choices=STATUS, default=0)

    # used while managing models from terminal
    def __str__(self):
        return self.title

    # meta for the class
    class Meta:
        ordering = ['-created_on']
  