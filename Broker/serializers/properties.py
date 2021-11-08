from rest_framework import serializers
from Broker.models.properties import Properties


class PropertiesSerializer(serializers.ModelSerializer):

	class Meta:
			model = Properties
			# agent
			# public_id
			# title
			# title_image_url
			# bedrooms
			# bathrooms
			# parking_spaces
			# location
			# property_type
			# updated_at
			# show_prices

			fields = '__all__'