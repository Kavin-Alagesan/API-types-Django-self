from rest_framework.views import APIView
from rest_framework.response import Response
from myapp.models import BlogModel
from myapp.serializers import BlogSerializer

class BlogAPIView(APIView):
    def get(self,request):
        blogs=BlogModel.objects.all()
        serializer=BlogSerializer(blogs,many=True)
        return Response({
            'success':True,
            'message':'GET request fulfilled!',
            'data':serializer.data
        })
    def post(self,request,*args,**kwargs):
        if request.data.get('title') != '':
            serializer=BlogSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                'success':True,
                'message':'POST request fulfilled!',
                'data':serializer.data
            })
    def put(self,request,*args,**kwargs):
        if request.data.get('id') is not None:
            blog=BlogModel.objects.get(pk=request.data.get('id'))
            if blog:
                serializer=BlogSerializer(blog,data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response({
                        'success':True,
                        'message':'PUT request fulfilled!',
                        'data':serializer.data
                    })
    def delete(self,request,*args,**kwargs):
        if request.data.get('id') is not None:
            blog=BlogModel.objects.get(pk=request.data.get('id'))
            if blog:
                blog.delete()
                return Response({
                        'success':True,
                        'message':'Delete request fulfilled!',
                        })
            
