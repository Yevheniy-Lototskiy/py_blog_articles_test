from django.urls import path
from .views import (
    article_list,
    article_detail,
    article_create,
    article_update,
    article_delete
)


urlpatterns = [
    path("", article_list, name="article_list"),
    path("<int:pk>/", article_detail, name="article_detail"),
    path("new/", article_create, name="article_create"),
    path("<int:pk>/edit/", article_update, name="article_update"),
    path("<int:pk>/delete/", article_delete, name="article_delete"),
]

app_name = "blog"
