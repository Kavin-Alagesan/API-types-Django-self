from rest_framework.response import Response
from rest_framework.decorators import api_view
from myapp.models import BlogModel
from myapp.serializers import BlogSerializer

@api_view(['GET','POST','PUT','DELETE'])
def blog_view(request):
    if request.method=='GET':
        blogs=BlogModel.objects.all()
        serializer=BlogSerializer(blogs,many=True)
        return Response({
            'success':True,
            'message':'GET request fulfilled!',
            'data':serializer.data
        })
    if request.method=='POST':
        if request.data.get('title') != '':
            serializer=BlogSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                'success':True,
                'message':'POST request fulfilled!',
                'data':serializer.data
            })

    if request.method=='PUT':
        if request.data.get('is') is not None:
            blog=BlogModel.objects.get(pk=request.data.get('id'))
            if blog:
                serializer=BlogSerializer(blog,data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response({
                        'success':True,
                        'message':'POST request fulfilled!',
                        'data':serializer.data
                    })

    return Response({
        'success':False,
        'message':'Invalid request!',
        'data':''
    })

