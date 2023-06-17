from django.db import models

# Create your models here.

class Sensordata(models.Model):
    humidity_val = models.FloatField(default=0.00)
    temperature_val = models.FloatField(default=0.00)
    moisture_val = models.FloatField(default=0.00)
    waterLevel_val = models.FloatField( default=0.00)

    def __str__(self):
            return f"Humidity: {self.humidity_val}, Temp: {self.temperature_val}, Moisture: {self.moisture_val}, waterLevel: {self.waterLevel_val}"