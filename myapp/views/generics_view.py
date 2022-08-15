from rest_framework import generics
from myapp.models import BlogModel
from myapp.serializers import BlogSerializer

class BlogListCreateAPI(generics.ListCreateAPIView):
    queryset=BlogModel.objects.all()
    serializer_class=BlogSerializer

class BlogListViewUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset=BlogModel.objects.all()
    serializer_class=BlogSerializer
