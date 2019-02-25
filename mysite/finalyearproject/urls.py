from django.urls import path
from . import views

app_name = "finalyearproject"

urlpatterns = [
    path("", views.homepage, name="homepage"),
]
