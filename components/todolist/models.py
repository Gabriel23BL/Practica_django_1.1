from django.db import models

class task(models.Model):
    subject = models.CharField(max_length=50)
    description = models.CharField(max_length=250)

    def __str__(self):
        return self.subject