from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Car(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=50)
    position = models.IntegerField(default=None)

    def __str__(self):
        return f"Car PK: {self.pk}  Car Name: {self.color} Car Color: {self.name}  Car Position: {self.position}"