from django.db import models

class Ideaticket(models.Model):
    idea_title = models.CharField(max_length=100)
    idea_no = models.IntegerField()
    idea_text = models.CharField(max_length=500)
    idea_link = models.CharField(max_length=100)
