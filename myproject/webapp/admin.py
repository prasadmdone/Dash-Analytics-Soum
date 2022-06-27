from django.contrib import admin

from .models import pagedata
from .models import gender


# Register your models here.
admin.site.register(pagedata)

admin.site.register(gender)
