from django.db import models

# Create your models here.
class SystemGeneration(models.Model):

    date = models.DateField(max_length=20, unique=True, verbose_name="Date")
    foundation_year = models.CharField(max_length=30, unique=True, verbose_name="Foundation generation")

    is_digital = models.BooleanField(default=False, verbose_name="Is Digital Network")
    system_status = models.CharField(max_length=50, default="OFFLINE", verbose_name="Current Status")

    summary = models.TextField(blank=True, null=True)

    generations = models.Manager()

    def __str__(self):
        return f"{self.date}: {self.foundation_year}"
