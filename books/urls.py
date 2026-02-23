from django.urls import path,include
from . import views

urlpatterns=[
    path('authors/',views.AuthorList.as_view(),name='authors'),
    path('login/',views.LoginView.as_view(),name='login'),
    path('logout/',views.LogoutView.as_view(),name='logout'),
    # path('api-auth/',include("rest_framework.urls")),
    path('books/',views.BookList.as_view(),name='books'),
    path('books/<slug:slug>/',views.BookDetail.as_view(),name='book_details'),
    path('users/',views.UserList.as_view(),name='user_list'),
]