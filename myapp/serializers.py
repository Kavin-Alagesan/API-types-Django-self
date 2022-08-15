from rest_framework import serializers
from myapp.models import BlogModel

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model=BlogModel
        fields='__all__'
