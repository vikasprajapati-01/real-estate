from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions

User = get_user_model()

class SignUpView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format = None):
        data = self.request.data

        name = data['name']
        email = data['email']
        password = data['password']
        confirm_password = data['confirm_password']

        if password == confirm_password:
            if User.objects.filter(email = email).exists():
                return Response({'error' : 'Email already exists'})
            else : 
                if len(password) < 6:
                    return Response({'error' : 'Password must have atleast 6 characters'})
                else:
                    user = User.objects.create_user(name=name, email=email, password=password)
                    user.save()
                    
                    return Response({'success': 'User created successfully'})
        else:
            return Response({'error': 'Password do not match'})        
        