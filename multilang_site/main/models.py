from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.CharField(max_length=500)
    publication_date = models.DateTimeField(auto_now_add=True)

class Meta:
    ordering = ['-publication_date']

class Document(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.title

class Ressource(models.Model):
    title = models.CharField(max_length=200)
    document = models.FileField()