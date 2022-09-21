from django.urls import path
from .views import SignUp,UserDetail, UserUpdate,Index,MyLoginView,MyPasswordChangeView,MyPasswordResetView,MyPasswordResetConfirmView,MyPasswordResetCompleteView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',Index.as_view(),name='index'),
    path('signup/',SignUp.as_view(),name='signup'),
    path('users/',UserDetail.as_view(),name='users'),
    path('user_detail/<int:pk>',UserUpdate.as_view(),name='user_detail'),
    path('login/',MyLoginView.as_view(),name='login'),
    path('logout/',auth_views.LogoutView.as_view(),name='logout'),
    path('change_password/',MyPasswordChangeView.as_view(),name='change_password'),
    path('password_reset/',MyPasswordResetView.as_view(),name='password_reset'),
    path('password_reset_confirm/',MyPasswordResetConfirmView.as_view(),name='password_reset'),
    path('password_reset_confirm/<uidb64>/<token>/',MyPasswordResetConfirmView.as_view(),name='password_reset'),
    path('password_reset_complete/',MyPasswordResetCompleteView.as_view(),name='password_reset'),
]

# path('',Index.as_view(),name='signup'),
#     path('signup/',SignUp.as_view(),name='signup'),
#     path('users/',UserDetail.as_view(),name='users'),
#     path('user_detail/<int:pk>',UserUpdate.as_view(),name='user_detail'),
#     path('login/',Login.as_view(),name='login'),
#     path('logout/',Logout.as_view(),name='logout'),
# ]