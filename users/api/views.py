from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from .serializers import RegistrationSerializer 

@api_view(['POST'])
def userRegistration(request):
    serializer = RegistrationSerializer(data = request.data)
    data = {}
    
    # check if the data is valid
    if serializer.is_valid():
        print('\nPrinting Validated Data')
        print(serializer.validated_data)
        # user_data = serializer.validated_data
        account = serializer.save()
        data['message'] = 'Registration Success'
        return Response(data, status = status.HTTP_201_CREATED)


    else:
        data = {"message": "No data given"}
        return Response(data, status = status.HTTP_400_BAD_REQUEST)

