import json
from django.http import HttpResponse, HttpResponseNotAllowed, JsonResponse
from django.views.generic import View
from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from api_v1.serializers import ArticleSerializer
from webapp.models import Article


@ensure_csrf_cookie
def get_token_view(request, *args, **kwargs):
    if request.method == 'GET':
        return HttpResponse()
    return HttpResponseNotAllowed('Only GET request are allowed')


class ArticleListView(View):
    def get(self, request, *args, **kwargs):
        objects = Article.objects.all()
        slr = ArticleSerializer(objects, many=True)
        return JsonResponse(slr.data, safe=False)


class ArticleDetailView(View):
    def get(self, request, *args, **kwargs):
        objects = get_object_or_404(Article, pk=pk)
        slr = ArticleSerializer(objects)
        return JsonResponse(slr.data, safe=False)


class ArticleCreateView(View):
    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        slr = ArticleSerializer(data=data)
        if slr.is_valid():
            article = slr.save()
            print(slr.data)
            return JsonResponse(slr.data, safe=False)
        else:
            response = JsonResponse(slr.errors, safe=False)
            response.status_code = 400
            return response


class ArticleUpdateView(View):
    def put(self, request, *args, **kwargs):
        saved_article = get_object_or_404(Article.objects.all(), pk=pk)
        data = request.data.get('article')
        slr = ArticleSerializer(instance=saved_article, data=data, partial=True)

        if slr.is_valid(raise_exception=True):
            article_saved = slr.save()

        return JsonResponse(slr.data, safe=False)


def ArticleDelete(self, request, *args, **kwargs):
    article = get_object_or_404(Article.objects.all(), pk=pk)
    article.delete()
    return Response({
        "message": "Article with id `{}` has been deleted.".format(pk)
    }, status=204)
