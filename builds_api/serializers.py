from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.PostSerializer): # serializers.ModelSerializer just tells django to convert sql to JSON
    class Meta:
        model = Post # tell django which model to use
        fields = ('id', 'name', 'cpu', 'cooler', 'mobo', 'ram', 'psu', 'gpu', 'storage', 'case',)