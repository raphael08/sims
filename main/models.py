from django.db import models

# Create your models here.

class Sensordata(models.Model):
    humidity_val = models.CharField(max_length=20)
    temperature_val = models.CharField(max_length=30)
    moisture_val = models.CharField(max_length=30)
    waterLevel_val = models.CharField(max_length=30, default=0)

    def __str__(self):
            return f"Humidity: {self.humidity_val}, Temp: {self.temperature_val}, Moisture: {self.moisture_val}, waterLevel: {self.waterLevel_val}"