from django.urls import path

from .views import (
    ArticleListView,
    ArticleDetailView,
    ArticleDeleteView,
    ArticleEditView,
    ArticleCreateView,
)

urlpatterns = [
    path("", ArticleListView.as_view(), name="articles"),
    path("create_article", ArticleCreateView.as_view(), name="create_article"),
    path("<int:pk>/", ArticleDetailView.as_view(), name="article_detail"),
    path("<int:pk>/delete/", ArticleDeleteView.as_view(), name="article_delete"),
    path("<int:pk>/edit/", ArticleEditView.as_view(), name="article_edit"),
]
