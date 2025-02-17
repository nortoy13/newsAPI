from rest_framework import serializers
from .models import News, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class NewsSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all()
    )

    class Meta:
        model = News
        fields = ['title', 'slug', 'content', 'created_at', 'is_published', 'category']
