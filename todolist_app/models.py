from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.


class Todo(models.Model):
    description = models.CharField(max_length=32)
    done = models.BooleanField(default=False)
    user_assigned = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    priority = models.ForeignKey(
        'Priority',
        on_delete=models.CASCADE,
    )


class Priority(models.Model):
    order = models.SmallIntegerField()
    description = models.CharField(max_length=32)

    def __str__(self):
        return self.description
