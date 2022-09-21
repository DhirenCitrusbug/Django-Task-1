from django.urls import path
from .views import Login, SignUp,UserDetail, UserUpdate,Index
urlpatterns = [
    path('',Index.as_view(),name='signup'),
    path('signup/',SignUp.as_view(),name='signup'),
    path('users/',UserDetail.as_view(),name='users'),
    path('user_detail/<int:pk>',UserUpdate.as_view(),name='user_detail'),
    path('login/',Login.as_view(),name='login')
]
