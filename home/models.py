from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    created = models.DateTimeField()

    def __str__(self):
        return self.title
