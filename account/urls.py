from django.urls import path,include

from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    #postviews
    #path('login/',views.user_login,name='login'),
    path('',views.dashboard,name='dashboard'),
    # path('login/',auth_views.LoginView.as_view(),name='login'),
    # path('logout/',auth_views.LogoutView.as_view(),name='logout'),

    # #change password
    # path('password_change/',auth_views.PasswordChangeView.as_view(),name='password_change'),
    # path('password_change/done/',auth_views.PasswordChangeDoneView.as_view(),name='password_change_done'),

    # #reset password
    # path('password_reset/',auth_views.PasswordResetView.as_view(),name='password_reset'),
    # path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    # path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    # path('reset/done/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),

        # ADVANTAGE OF django.contrib.auth(above all path include in a single path)
    path('',include('django.contrib.auth.urls')),

    path('register/',views.register,name='register'),
    path('edit/',views.edit,name='edit'), #go to profile edit path 

]
