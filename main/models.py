from django.db import models


class Task(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DetaTimeField(auto_now_add=True)
    status = models.IntegerField(choices=(
        (1, 'active'),
        (2, 'finished'),
    ), default=1)