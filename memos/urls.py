from django.urls import path
from . import views


app_name = "memos"

urlpatterns = [
    path('', views.index, name="index"),
    path('add', views.add, name="add"),
    path('detail/<mpk>', views.detail, name="detail"),
    path('modify/<mpk>', views.modify, name="modify"),
]
