from django.urls import path

from api_v1.views import get_token_view, ArticleListView, ArticleCreateView, ArticleDetailView, ArticleUpdateView, ArticleDelete

app_name = 'api_v1'

urlpatterns = [
    path('get-token/', get_token_view, name='get_token'),
    path('articles/', ArticleListView.as_view(), name='article_list'),
    path('articles/detail/', ArticleDetailView.as_view(), name='article_detail'),
    path('article/create/', ArticleCreateView.as_view(), name='article_create'),
    path('article/update/', ArticleUpdateView.as_view(), name='article_update'),
    path('article/delete/', ArticleDelete.as_view(), name='article_delete'),
]
