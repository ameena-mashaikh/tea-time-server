from django.db import models


class TeaDetails(models.Model):
    tea_id = models.ForeignKey(
        "TeaListing", on_delete=models.CASCADE, related_name="tea_listing")
    alternate_names = models.CharField(max_length=60)
    origin = models.CharField(max_length=60)
    tea_type = models.CharField(max_length=20)
    description = models.CharField(max_length=700)
    color = models.CharField(max_length=20)
    taste = models.CharField(max_length=100)
    caffeine_level = models.CharField(max_length=50)
