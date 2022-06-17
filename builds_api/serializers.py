from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Post
        fields = ('id', 'name', 'description', 'cpu', 'cooler', 'mobo', 'ram', 'psu', 'gpu', 'storage', 'case', 'img',)