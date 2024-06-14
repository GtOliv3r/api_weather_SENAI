from typing import Any
from datetime import datetime
from random import randrange
from django.http import HttpRequest
from django.http.response import HttpResponse as HttpResponse
from django.views import View
from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from user.forms import UserForm
from user.repositories import UserRepository
from user.serializers import UserSerializer
from .authentication import *
from user.utils import generate_token

class AuthUser(View):
    def get(self, request):
        user = authenticate(username = 'user', password = 'password')
        if user:
                token = generate_token(user)
                response = redirect('Weather View')
                response.set_cookie('jwt', token)
                return response 
        return redirect('Weather View')
    

class UnAuthUser(View):
    def get (self,request):
        response = redirect('Weather View')
        response.delete_cookie('jwt')
        return response

class UserInsert(View):

    def get(self, request):
        userForm = UserForm()
        return render(request, "form_user.html", {"form": userForm})
    
    def post(self, request):
        print("Tentando fazer o POST")
        userForm = UserForm(request.POST)
        if userForm.is_valid():
            print("Formulário válido")
            serializer = UserSerializer(data=userForm.data)
            if serializer.is_valid():
                print("Serializer válido, salvando na coleção")
                repository = UserRepository(collectionName='users')
                print("Dados a serem inseridos:", serializer.data)
                repository.insert(serializer.data)
                print("Dados inseridos com sucesso:", serializer.data)
            else:
                print("Erros do serializer:", serializer.errors)
        else:
            print("Erros do formulário:", userForm.errors)

        return redirect('User View')

class UserTokenizer(View):
    # método deveria ser POST, pois deverá receber usuario e senha
    def get(self, request):
        user = authenticate(username='user', password='a1b2c3')
        if user:
            return HttpResponse(generateToken(user))
        return HttpResponse('Username and/or password incorret')
    
