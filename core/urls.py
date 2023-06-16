from django.contrib.auth import views as auth_views
from django.urls import path
from puddle import settings
from . import views
from .forms import LoginFormWithEmailVerification

app_name = 'core'

urlpatterns = [
    path('', views.index,name='index'),
    path('verification/', views.wait_for_verification, name='wait_for_verification'),
    path('contact/', views.contact, name='contact'),
    path('avatar/', views.change_avatar, name='avatar'),
    path('verify/<str:token>', views.verify, name='verify_email'), 
    path('signup/', views.signup, name='signup'),
    path('profile/<int:pk>/', views.profile, name='profile'),
    path('logout/', auth_views.LogoutView.as_view(next_page=settings.LOGOUT_REDIRECT_URL), name='logout'),
    path('login/', auth_views.LoginView.as_view(
        template_name='core/login.html',
        authentication_form=LoginFormWithEmailVerification,
        redirect_authenticated_user=True
    ), name='login'),
]