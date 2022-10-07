from random import sample
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import FileUploadParser
from .serializers import FileSerializer

import io
import minio


# import and connect to mongodb
import pymongo
mongoClient = pymongo.MongoClient("mongodb://localhost:27017")
db = mongoClient['redd']





# file upload
@api_view(['POST'])
def fileUpload(request):
    # get file
    # get the file metadata




    someText = "text of some file"
    value_bytes = someText.encode('utf-8')
    value_stream = io.BytesIO(value_bytes)
    print(type(value_bytes))
    print(type(value_stream))
    
    file = request.FILES.get('file')
    # destination = open('some_file.txt', 'wb+')
    val = ".".encode('utf-8')
    print((file.chunks()))
    for chunk in file.chunks():
        val += chunk
        # print(type(chunk))
    print(val)

















    # for chunk in file.chunks():
    #     destination.write(chunk)
    # destination.close()
    


    # parser_classes = (FileUploadParser,)
    # file_obj = request.data['file']
    # print(file_obj)
    # print(request.FILES.get('file'))
    
    # print(file_obj)
    # print(parser_classes)
    # serializer = FileSerializer(data=request.FILES.get('file'))
    # print('Printing serializer \n')
    # print(serializer)
    



    # sample_file = request.FILES.get('file')
    # with open(sample_file, 'r') as f:
    #     print(f.read())
    # print(request.FILES)
    return Response({'message': 'Files'})
    pass
