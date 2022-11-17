from rest_framework import serializers
from api.models import Products,Carts,Reviews





class CartSerializer(serializers.ModelSerializer):
    product=serializers.CharField(read_only=True)
    user=serializers.CharField(read_only=True)
    date=serializers.DateField(read_only=True)

    class Meta:
        model=Carts 
        fields=["product","user","date"]
    def create(self, validated_data):
        user=self.context.get("user")
        product=self.context.get("product")
        return Carts.objects.create(
            **validated_data,
            user=user,
            product=product
        )

class ReviewSerializer(serializers.ModelSerializer):
    product=serializers.CharField(read_only=True)
    user=serializers.CharField(read_only=True)
    class Meta:
        model=Reviews
        fields="__all__"

    def create(self, validated_data):
        user=self.context.get("user")
        product=self.context.get("product")
        return Reviews.objects.create(**validated_data,user=user,product=product)

class ProductSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    product_reviews=ReviewSerializer(read_only=True,many=tuple)

    class Meta:
        model=Products
        fields="__all__"