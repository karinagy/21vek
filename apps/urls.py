from django.urls import include, path

urlpatterns = [
    path("main/", include("apps.main.urls")),
]
