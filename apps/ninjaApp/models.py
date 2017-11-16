from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Dojo(models.Model):
  name = models.CharField(max_length=255)
  city = models.CharField(max_length=255)
  state = models.CharField(max_length=2)
  desc = models.TextField(blank=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  def __repr__(self):
      return "Dojo Object :: {} {} {} {}".format(self.name, self.city, self.state, self.desc)
class Ninja(models.Model):
  first_name = models.CharField(max_length=255)
  last_name = models.CharField(max_length=255)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  dojo = models.ForeignKey(Dojo, related_name="ninjas", null=True)
  def __repr__(self):
      return "ninja object:: {} {} ".format(self.first_name, self.last_name)
'''
Shell Commands
from apps.ninjaApp.models import *
Dojo.objects.create(name="CodingDojo Silicon Valley", city = "Mountain View", state= "CA")
Dojo.objects.create(name="CodingDojo Seattle", city = "Seattle", state= "WA")
Dojo.objects.create(name="CodingDojo New York", city = "New York", state= "NY")
Dojo.objects.create(name="CodingDojo Texas", city = "Dallas", state= "DY")

dojo1=Dojo.objects.get(id=1)
dojo2=Dojo.objects.get(id=2)
dojo3=Dojo.objects.get(id=3)

Create 3 ninjas that belong to the first dojo you created.
Create 3 more ninjas and have them belong to the second dojo you created.
Create 3 more ninjas and have them belong to the third dojo you created.

Ninja.objects.create(first_name="Mary",last_name="Jane", dojo = dojo1)
Ninja.objects.create(first_name="Martha",last_name="Simpson", dojo = dojo1)
Ninja.objects.create(first_name="Raja",last_name="sunder", dojo = dojo1)
Ninja.objects.create(first_name="Jack",last_name="Sprat", dojo = dojo2)
Ninja.objects.create(first_name="Maria",last_name="Gonzalez", dojo = dojo2)
Ninja.objects.create(first_name="Jackly",last_name="Fernandez", dojo = dojo2)
Ninja.objects.create(first_name="Samantha",last_name="Drasher", dojo = dojo3)
Ninja.objects.create(first_name="Arun",last_name="Ragunath", dojo = dojo3)
Ninja.objects.create(first_name="Raj",last_name="Parthasarthy", dojo = dojo3)

Be able to retrieve all ninjas that belong to the first Dojo
dojoLast = Dojo.objects.last().id
Ninja.objects.all().filter(dojo=dojoFirst)

Be able to retrieve all ninjas that belong to the last Dojo
dojoFirst = Dojo.objects.first().id
Ninja.objects.all().filter(dojo=dojoLast)

'''