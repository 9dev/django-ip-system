from django.views.generic import CreateView, DetailView

from .forms import ArticleForm
from .models import Article


class ArticleCreateView(CreateView):
    model = Article
    form_class = ArticleForm


class ArticleDetailView(DetailView):
    model = Article
