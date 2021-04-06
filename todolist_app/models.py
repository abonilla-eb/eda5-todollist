from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.


class Todo(models.Model):
    class Meta:
        ordering = ['priority']

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

    def __str__(self):
        return f'{self.description} ({"done" if self.done else "todo"})'


class Priority(models.Model):
    class Meta:
        ordering = ['order']

    order = models.SmallIntegerField()
    description = models.CharField(max_length=32)

    def __str__(self):
        return self.description
