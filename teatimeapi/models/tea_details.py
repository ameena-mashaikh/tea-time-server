from django.db import models


class TeaDetails(models.Model):
    name = models.CharField(max_length=60)
    image = models.CharField(max_length=500)
    origin = models.CharField(max_length=60)
    tea_type = models.CharField(max_length=20)
    # tea_type_num = models.ForeignKey(
    #     "TeaType", on_delete=models.CASCADE, related_name="tea_type_for_tea_detail")
    description = models.CharField(max_length=700)
    color = models.CharField(max_length=20)
    taste = models.CharField(max_length=100)
    caffeine = models.CharField(max_length=50)
