from django.contrib import admin

# Register your models here.
from .models import User,EmailVerificationToken

admin.site.register(User)
admin.site.register(EmailVerificationToken)