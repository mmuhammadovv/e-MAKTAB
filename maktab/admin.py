from django.contrib import admin

# Register your models here.


from .models import *


admin.site.register(User)
admin.site.register(Pupil)
admin.site.register(Teacher)
admin.site.register(PupilProfile)
admin.site.register(Lesson)