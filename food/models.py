from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.deletion import CASCADE

class Food(models.Model):
    dish = models.CharField(max_length=256)
    customer = models.ForeignKey(get_user_model(), on_delete=CASCADE)
    description = models.TextField(default="", null=True, blank=True)

    def __str__(self):
        return self.name
