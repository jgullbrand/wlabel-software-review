from django.contrib import admin
from .models import SoftwareProduct, Reviews, Category

admin.site.register(SoftwareProduct)
admin.site.register(Reviews)
admin.site.register(Category)