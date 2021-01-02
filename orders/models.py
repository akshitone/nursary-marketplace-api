from django.db import models
from core.models import Plant, User


class Order(models.Model):
    plant = models.ForeignKey(Plant, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
