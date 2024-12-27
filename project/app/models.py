from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=25)
    author = models.CharField(max_length=25)

    def __str__(self):
        return self.title

    def full_name(self):
        return self.title + '-' + self.author
