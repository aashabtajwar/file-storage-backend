# from webbrowser import get
# from http.client import HTTPResponse
from django.urls import reverse

from django.http import HttpResponse, JsonResponse
from django.conf import settings
from rest_framework.response import Response

import jwt


secret = "secret"

class AuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        print(get_response)

    def __call__(self, request):
        # print(request)
        # print('Printing request')
        # print(request)
        response = self.get_response(request)
        # print('PRINTING response')
        # print(response)
        return response


    def process_view(self, request, view_func, view_args, view_kwargs):
        """
        - check if token exists
        - if it does check if it has expired
        - if it has not expired, check url
           - if the url is from login or register, don't allow
        - if it did expire, check the url again
           - for login and register allow
           - otherwise don't
        """


        """
        --------------------------  REDUNDANCY ALERT!  ---------------------------------
        The code below is very redundant! Try to reduce the redundancy to improve quality
        
        """

        # get token
        print(request.META['PATH_INFO'] == '/api/user/login/')
        token = request.META.get('HTTP_AUTHORIZATION')

        # if there is no token
        if token is None:
            # check if url is anything other than login or register
            print('Should follow here')
            if (request.META['PATH_INFO'] != '/api/user/login/') or (request.META['PATH_INFO'] != '/api/user/register/'):
                print('why is this invoking')
                return JsonResponse({"message": "Unauthorized"}, status = 401)
        
        # if there is a token
        else:
            # check if token has expired
            try:
                jwt.decode(token, secret, algorithms="HS256")
                
                # token is still active
                # do not allow for login and register
                if request.META['PATH_INFO'] == '/api/user/login/' or request.META['PATH_INFO'] == '/api/user/register/':
                    return JsonResponse({"message": "Unauthorized"}, status = 401)

            except jwt.ExpiredSignatureError:
                # token has expired
                # do not allow anything other than login or register 
                if request.META['PATH_INFO'] != '/api/user/login/' or request.META['PATH_INFO'] != '/api/user/register/':
                    return JsonResponse({"message": "Unauthorized"}, status = 401)

        # print('Printing relative url')
        # print(request.META['PATH_INFO'])
        # # get token
        # token = request.META.get('HTTP_AUTHORIZATION')
        # try:
        #     jwt.decode(token, secret, algorithms="HS256")
        # except jwt.ExpiredSignatureError:
        #     # check url
        #     # if url is login
        #     return JsonResponse({"message": "Expired"})


        # verify if the token exists

        # print(token)
        # print('request:  ')
        # print(request)
        # print('view Func:  ')
        # print(view_func)
        # print('view args:  ')
        # print(view_args)
        # print('view kwargs:  ')
        # print(view_kwargs)