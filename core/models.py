from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


class Pledge(models.Model):
  amount = models.IntegerField()
  date = models.DateField(auto_now_add=True)
  user = models.ForeignKey(User)


  def get_absolute_url(self):
    return reverse("pledge_detail", args=[self.id])

class Contribution(models.Model):
  amount = models.IntegerField()
  date = models.DateField(auto_now_add=True)
  notes = models.CharField(max_length=50)
  user = models.ForeignKey(User)


  def __unicode__(self):
    return self.notes

  def get_absolute_url(self):
    return reverse("contribution_detail", args=[self.id])

class UserProfile(models.Model):
  user = models.OneToOneField(User, related_name='user', on_delete=models.CASCADE)
  state = models.CharField(max_length=50, blank=True, null=True)

  def __unicode__(self):
    return "%s profile" % (self.user.username)

# Create your models here.
