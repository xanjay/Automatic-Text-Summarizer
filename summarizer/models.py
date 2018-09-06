from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Summary(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()  #limit or not
    original_link = models.TextField() ##auto delete option
    date_created = models.DateTimeField()

    def __str__(self):
        return self.original_link
