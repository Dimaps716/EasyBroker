from django.contrib.postgres.fields import JSONField
from django.db import models


class Properties(models.Model):
  """
  represent Properties.
  """
  agent = models.CharField(max_length=80, null=True, blank=True)
  public_id = models.CharField(max_length=20, null=True, blank=True)
  title = models.CharField(max_length=100, null=True, blank=True)
  title_image_url = models.URLField(max_length=200, null=True, blank=True)
  bedrooms = models.IntegerField()
  bathrooms = models.IntegerField()
  parking_spaces = models.IntegerField()
  location = models.CharField(max_length=100, null=True, blank=True)
  property_type = models.CharField(max_length=100, null=True, blank=True)
  operations = JSONField()
  updated_at = models.DateField()
  show_prices = models.BooleanField(default=False)
