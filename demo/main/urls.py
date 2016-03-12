from django.conf.urls import url

from main import views


urlpatterns = [
    url(
        r'^$',
        views.ArticleListView.as_view(),
        name='article_list'
    ),
    url(
        r'^create$',
        views.ArticleCreateView.as_view(),
        name='article_create'
    ),
    url(
        r'^article/(?P<pk>[0-9]+)',
        views.ArticleDetailView.as_view(),
        name='article_detail'
    ),
]
