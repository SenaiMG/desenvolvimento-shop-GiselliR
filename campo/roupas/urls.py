from django.urls import path

from . import views


urlpatterns = [
    path('pagina/', views.index, name="index"),
    path("", views.pagina, name="pagina")
]