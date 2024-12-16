from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    #here we can use the custom validation on price.
    def validate_price(self, value):
        if value < 0:
            raise serializers.ValidationError("Price must be in positive")
        return value

