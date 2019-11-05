from django.contrib import admin
from .models import MyUser, Item, Category
# Register your models here.
admin.site.register(MyUser)
admin.site.register(Item)
admin.site.register(Category)