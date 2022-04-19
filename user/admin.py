from django.contrib import admin

# Register your models here.
from .models import *
from .models import User , user_type

admin.site.register(user_type)
admin.site.register(User)
admin.site.register(House)
admin.site.register(Room)
admin.site.register(Contact)
