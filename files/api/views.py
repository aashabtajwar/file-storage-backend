from random import sample
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import FileUploadParser
from .serializers import FileSerializer


import io
from minio import Minio


# import and connect to mongodb
import pymongo
mongoClient = pymongo.MongoClient("mongodb://localhost:27017")
db = mongoClient['redd']

# set up min io
minioBucket = Minio(
    "localhost:9000",
    access_key="minioadmin",
    secret_key="minioadmin",
    secure=False
)
bucket_name = "djangofilestorage"



# trying out a class based view
class GetTest(APIView):
    def get(self, request, format = None):
        return Response({"message": "Testing class based view"})


# file upload
class UploadFile(APIView):
    # @route - post - upload file
    def post(self, request, format=None):
        # get file
        # get the file metadata
        # store the metadata in mongodb
        # store the file in minio



        # get file metadata (file type, file size, file name)
        # get additional metadata -> user_id, username
        file = request.FILES.get('file')
        file_metadata = {
            'file_size' : file.size,
            'file_type' : file.content_type,
            'file_name' : file.name,
        }
            # store the data in mongoDB
        collection = db['fileMetaData']
        insert = collection.insert_one(file_metadata)
        file_id = str(insert.inserted_id)

        # now handle file
        fileBytes = '.'.encode('utf-8')
        for chunk in file.chunks():
            fileBytes += chunk
        fileValueStream = io.BytesIO(fileBytes)
        
        minioBucket.put_object("djangofilestorage", file_id, fileValueStream, length=len(fileBytes))

        return Response({"message": "Successfully Uploaded File"})


# file upload
@api_view(['POST'])
def fileUpload(request):
    # get file
    # get the file metadata
    # store the metadata in mongodb
    # store the file in minio
    

    # get file metadata (file type, file size, file name)
    # get additional metadata -> user_id, username
    # the db will take care of the created_at and updated_at metadata    
    file = request.FILES.get("file")
    file_metadata = {
        'file_size' : file.size,
        'file_type' : file.content_type,
        'file_name' : file.name,
    }
    # store the data in mongoDB
    collection = db['fileMetaData']
    insert = collection.insert_one(file_metadata)
    file_id = str(insert.inserted_id)

    # now handle file
    fileBytes = '.'.encode('utf-8')
    for chunk in file.chunks():
        fileBytes += chunk
    fileValueStream = io.BytesIO(fileBytes)
    
    minioBucket.put_object("djangofilestorage", file_id, fileValueStream, length=len(fileBytes))


    # store 



    # get relevant metadata
    




    # someText = "text of some file"
    # value_bytes = someText.encode('utf-8')
    # value_stream = io.BytesIO(value_bytes)
    # print(type(value_bytes))
    # print(type(value_stream))
    
    # file = request.FILES.get('file')
    # # destination = open('some_file.txt', 'wb+')
    # val = ".".encode('utf-8')
    # print((file.chunks()))
    # for chunk in file.chunks():
    #     val += chunk
    #     # print(type(chunk))
    # print(val)

















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
