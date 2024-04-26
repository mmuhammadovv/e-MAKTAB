from django.contrib import admin
from .models import *

# admin 
admin.site.register(Contact)
admin.site.register(Video)
admin.site.register(User)
admin.site.register(AccountType)