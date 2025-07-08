from django.db import models

class MainModel(models.Model):
    name = models.CharField(max_length=255)
    value = models.IntegerField()
    
    def __str__(self):
        return "ID: " + str(self.id) + " NAME: " + str(self.name) + " VALUE: " + str(self.value)