from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from Broker.models import Properties


class PropertiesTests(APITestCase):

  def create_objects(self):
    data =[
      {
      "agent": "John Smith",
      "public_id": "EB-XXX123",
      "title": "Beautiful property in Condesa",
      "title_image_url": "https://www.easybroker.com/assets/product/logo-be4da843987ccd1c05e26f8703f1787847471b36d08bdb1ec8a91ce4007b0e98.svg",
      "bedrooms": 0,
      "bathrooms": 0,
      "parking_spaces": 0,
      "location": "Condesa, Cuauhtemoc",
      "property_type": "Apartment",
      "operations": [
        {
          "type": "sale",
          "amount": 500000,
          "formated_amount": "US$ 500,000",
          "currency": "USD",
          "unit": "total"
        },
        {
          "type": "temporary_rental",
          "amount": 500,
          "formated_amount": "US$ 500",
          "currency": "USD",
          "period": "monthly"
        }
      ],
      "updated_at": "2020-03-01T23:26:53.402Z",
      "show_prices": True
      }
    ]
    data = Properties.objects.bulk_create(data)

  def test_Properties(self):
    self.assertEqual(Properties.objects.all().count(), 1)
