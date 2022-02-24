from django.db import models
from django.contrib.auth.models import User

class Room(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to="rooms", null=True)


class Container(models.Model):
    name = models.CharField(max_length=200)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to="containers", null=True)


class Subcontainer(models.Model):
    name = models.CharField(max_length=200)
    container = models.ForeignKey(Container, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to="subcontainers", null=True)


class Object(models.Model):
    name = models.CharField(max_length=200)
    subcontainer = models.ForeignKey(Subcontainer, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to="objects", null=True)
    public = models.IntegerField(default=0)
    details = models.TextField(null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()


class ViewLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    object = models.ForeignKey(Object, on_delete=models.CASCADE)
    created_at = models.DateTimeField()