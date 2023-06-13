from django.db import models


class Teas(models.Model):
    name = models.CharField(max_length=60)
    image = models.CharField(max_length=500)
    origin = models.CharField(max_length=60)
    tea_type = models.ForeignKey(
        "TeaType", on_delete=models.CASCADE, related_name="tea_types")
    description = models.CharField(max_length=700)
    color = models.CharField(max_length=20)
    taste = models.CharField(max_length=100)
    caffeine = models.CharField(max_length=50)
