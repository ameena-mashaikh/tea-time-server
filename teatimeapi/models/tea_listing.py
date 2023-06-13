from django.db import models


class TeaListing(models.Model):
    name = models.CharField(max_length=60)
    image = models.CharField(max_length=500)
