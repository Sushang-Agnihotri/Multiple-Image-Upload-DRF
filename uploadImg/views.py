from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView
from .models import PropertyImage
from .serializers import PropertyImageSerializers

# Create your views here.
class PhotoUploadView(ListCreateAPIView):
    queryset = PropertyImage.objects.all()
    serializer_class = PropertyImageSerializers
    def post(self, request, *args, **kwargs):
        username = request.data['username']
        form_data = {}
        form_data['username']= username
        success = True
        response = []
        for images in request.FILES.getlist('images'):
            form_data['images']=images
            print(form_data)
            serializer = PropertyImageSerializers(data=form_data)
            if serializer.is_valid():
                serializer.save()
                response.append(serializer.data)
            else:
                success = False
        if success:
            return Response({
                'status' : 1, 
                'message' : 'Success',
                'Data' : response,
            })
        return Response({
                'status' : 0, 
                'message' : 'Error!',
            })    
