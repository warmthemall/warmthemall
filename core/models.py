from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

class Pledge(models.Model):
  amount = models.IntegerField()
  date = models.DateField(auto_now_add=True)
  user = models.ForeignKey(User)

  def __unicode__(self):
    return self.title

class Contribution(models.Model):
  amount = models.IntegerField()
  date = models.DateField(auto_now_add=True)
  notes = models.CharField(max_length=50)
  user = models.ForeignKey(User)

  def __unicode__(self):
    return self.title
# Create your models here.
