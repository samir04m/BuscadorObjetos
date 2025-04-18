from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Room(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to="rooms", null=True, blank=True)

    def save(self, *args, **kwargs):
        super(Room, self).save(*args, **kwargs)
        if self.photo:
            image = Image.open(self.photo.path)
            image.save(self.photo.path, quality=20, optimize=True)

    def __str__(self):
        return str(self.name)


class Container(models.Model):
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to="containers", null=True, blank=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        super(Container, self).save(*args, **kwargs)
        if self.photo:
            image = Image.open(self.photo.path)
            image.save(self.photo.path, quality=20, optimize=True)

    def __str__(self):
        return "{} ({})".format(self.name, self.room.name)


class SubContainer(models.Model):
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to="subContainers", null=True, blank=True)
    container = models.ForeignKey(Container, on_delete=models.CASCADE)

    class Meta:
        ordering = ['name']

    def save(self, *args, **kwargs):
        super(SubContainer, self).save(*args, **kwargs)
        if self.photo:
            image = Image.open(self.photo.path)
            image.save(self.photo.path, quality=20, optimize=True)

    def __str__(self):
        return "{} ({})".format(self.name, self.container.name)


class Object(models.Model):
    name = models.CharField(max_length=200)
    public = models.BooleanField(default=True)
    details = models.CharField(max_length=250, null=True, blank=True)
    photo = models.ImageField(upload_to="objects", null=True, blank=True)
    subContainer = models.ForeignKey(SubContainer, on_delete=models.CASCADE)

    class Meta:
        indexes = [
            models.Index(fields=['name']),
            models.Index(fields=['public']),
        ]

    def save(self, *args, **kwargs):
        super(Object, self).save(*args, **kwargs)
        if self.photo:
            image = Image.open(self.photo.path)
            image.save(self.photo.path, quality=20, optimize=True)

    def __str__(self):
        return str(self.name)


class ViewLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    object = models.ForeignKey(Object, on_delete=models.CASCADE)
    last_seen = models.DateTimeField()

    class Meta:
        ordering = ['-last_seen']

    def __str__(self):
        return "{} - {}".format(self.user.username, self.object.name)