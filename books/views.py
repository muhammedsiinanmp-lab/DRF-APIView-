from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Book
from .serializers import BookSerializer,AuthorSerializer,UserCreationSerializer
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from rest_framework.permissions import AllowAny,IsAuthenticated


class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self,request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username,password=password)

        if user is not None:
            login(request,user)
            return Response({"message":"Login Successfull"})
        return Response({"error":"Invalid Credentials"},status=status.HTTP_400_BAD_REQUEST)
    
class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        logout(request)  
        return Response({"message": "Logged out"})

class AuthorList(APIView):

    permission_classes = [IsAuthenticated]

    def get(self,request):
        authors = User.objects.all()
        serializer = AuthorSerializer(authors,many=True)
        return Response(serializer.data)
    
class UserList(APIView):

    def get(self,request):
        authors = User.objects.all()
        serializer = UserCreationSerializer(authors,many=True)
        return Response(serializer.data)

    def post(self,request):
        
        serializer = UserCreationSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class BookList(APIView):

    def get(self,request):
        books = Book.objects.all()
        serializer = BookSerializer(books,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        many = isinstance(request.data,list)
        serializer = BookSerializer(data=request.data,many=many)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class BookDetail(APIView):

    def get(self,request,slug):
        book = get_object_or_404(Book,slug=slug)
        serializer = BookSerializer(book)
        return Response(serializer.data)
    
    def put(self,request,slug):
        book = get_object_or_404(Book,slug=slug)
        serializer = BookSerializer(book,data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self,request,slug):
        book = get_object_or_404(Book,slug=slug)
        serializer = BookSerializer(book,data=request.data,partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,slug):
        book = get_object_or_404(Book,slug=slug)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
