from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from .serializers import RegistrationSerializer, UserSerializer 
from .backends import CustomAuthentication, TokenJWT

from .backends import CustomAuthentication

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



@api_view(['POST'])
def userLogin(request):
    print(request.data)
    email = request.data['email']
    password = request.data['password']
    print('THIS FAR')
    user = CustomAuthentication.authenticate(request, email, password)
    if user is None:
        return Response({'message': 'Invalid'})
    

    # val = user.email
    # print("Printing User\n")
    # print(val)
    # generate jwt token
    instance = TokenJWT()
    token = instance.generateJWT(user.username, user.email)
    return Response({"message": "Login Success", "token": token})

    # serializer = UserSerializer(data = user)
    # if serializer.is_valid():
    #     # generate jwt token
    #     instance = TokenJWT()
    #     # token = instance.generateJWT(user.username, user.email)
    #     print(serializer.data)
    #     return Response({"message": serializer.data})
