from django.db import models

# Create your models here.


class toDolists():
    title = models.CharField(max_length=108)
    description = models.TextField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title

