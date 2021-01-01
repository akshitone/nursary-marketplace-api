from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Plant(models.Model):
    name = models.TextField()
    price = models.FloatField(default=0)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
