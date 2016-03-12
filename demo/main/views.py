from django.views.generic import CreateView, DetailView, ListView

from ip_system.models import Ip

from .forms import ArticleForm
from .models import Article


class ArticleCreateView(CreateView):
    model = Article
    form_class = ArticleForm

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author_ip = Ip.get_or_create(request=self.request)
        return super(ArticleCreateView, self).form_valid(form)


class ArticleDetailView(DetailView):
    model = Article


class ArticleListView(ListView):
    model = Article
