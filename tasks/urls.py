from django.urls import path
from .views import create_item, show_items

urlpatterns = [
    path('createtask', create_item, name="create_item"),
    path('', show_items, name="show_items")
]