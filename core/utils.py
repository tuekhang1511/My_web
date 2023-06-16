from django.core.mail import send_mail
from django.conf import settings

def send_email_token(email,token):
    try:
        subject = 'Your account needs to be verified'
        message = f'Click on the link to verify http://127.0.0.1:8000/verify/{token}'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email, ]
        send_mail( subject, message, email_from, recipient_list )
    except Exception as e:
        return False
    
    return True

# from django.contrib.auth.backends import ModelBackend

# class EmailVerificationBackend(ModelBackend):
#     def authenticate(self, request, username=None, password=None, **kwargs):
#         user = super().authenticate(request, username=username, password=password, **kwargs)
        
#         if user and user.email_verified:
#             return user
        
#         return None
