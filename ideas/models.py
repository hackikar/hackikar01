from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Ideaticket(models.Model):
    idea_title = models.CharField(max_length=100)
    idea_no = models.IntegerField()
    idea_text = models.CharField(max_length=500)
    idea_link = models.CharField(max_length=100)
    author = models.ForeignKey('auth.User')
    created_date = models.DateTimeField(
            default=timezone.now)
