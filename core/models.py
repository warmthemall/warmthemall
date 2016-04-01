from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

class Pledge(models.Model):
  amount = models.IntegerField()
  date = models.DateField(auto_now_add=True)
  user = models.ForeignKey(User)

  def __unicode__(self):
    return self.title

  def get_absolute_url(self):
    return reverse("pledge_detail", args=[self.id])

class Contribution(models.Model):
  amount = models.IntegerField()
  date = models.DateField(auto_now_add=True)
  notes = models.CharField(max_length=50)
  user = models.ForeignKey(User)

  def __unicode__(self):
    return self.title

  def get_absolute_url(self):
    return reverse("contribution_detail", args=[self.id])
# Create your models here.
