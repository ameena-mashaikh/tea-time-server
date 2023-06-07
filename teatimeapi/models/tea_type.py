from django.db import models


class TeaType(models.Model):
    tea_type = models.CharField(max_length=30)
