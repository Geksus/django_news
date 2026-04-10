from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    DeleteView,
    UpdateView,
    CreateView,
)

from articles.models import Article


# Create your views here.
class ArticleListView(ListView):
    model = Article
    template_name = "article_list.html"
    context_object_name = "articles"

    def get_queryset(self):
        sort = self.request.GET.get("sort") or "-date"
        allowed = {"author", "date", "-date"}
        if sort in allowed:
            return Article.objects.order_by(sort)
        return Article.objects.all()


class ArticleDetailView(DetailView):
    model = Article
    template_name = "article_detail.html"


class ArticleDeleteView(DeleteView):
    model = Article
    success_url = reverse_lazy("articles")

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)


class ArticleEditView(UpdateView):
    model = Article
    template_name = "article_edit.html"
    fields = ["title", "body"]
    success_url = "/articles/"


class ArticleCreateView(CreateView):
    model = Article
    template_name = "article_create.html"
    fields = ["title", "body", "author"]
    success_url = reverse_lazy("articles")
