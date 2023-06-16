from django.contrib.auth import views as auth_views
from django.urls import path
from puddle import settings
from . import views
from .forms import LoginForm, EmailVerificationAuthenticationForm

app_name = 'core'

urlpatterns = [
    path('', views.index,name='index'),
    path('verification-success/', views.verification_success, name='verification_success'),
    path('verification-failed/', views.verification_failed, name='verification_failed'),
    path('contact/', views.contact, name='contact'),
    path('avatar/', views.change_avatar, name='avatar'),
    path('verify/<str:token>', views.verify, name='verify_email'), 
    path('signup/', views.signup, name='signup'),
    path('profile/<int:pk>/', views.profile, name='profile'),
    path('logout/', auth_views.LogoutView.as_view(next_page=settings.LOGOUT_REDIRECT_URL), name='logout'),
    path('login/', auth_views.LoginView.as_view(
        template_name='core/login.html',
        authentication_form=EmailVerificationAuthenticationForm,
        redirect_authenticated_user=True
    ), name='login'),
]