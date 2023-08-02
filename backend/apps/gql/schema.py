import graphene
from graphene_django import DjangoObjectType
from graphene import relay
from django_filters.filterset import FilterSet
from graphene_django.filter.fields import DjangoFilterConnectionField
from django.shortcuts import get_object_or_404

from blog.models import Article


class ArticleFilterset(FilterSet):
    class Meta:
        model = Article
        fields = {
            "tags__name": ('exact', 'contains'),
            "slug": ("exact",)
        }


class ArticleNode(DjangoObjectType):
    user = graphene.JSONString()
    tags = graphene.JSONString()
    
    class Meta:
        model = Article
        filterset_class = ArticleFilterset
        interfaces = [relay.Node]
        fields = [
            "title",
            "subtitle",
            "thumbnail",
            "slug",
            "tags",
            "article",
            "user",
            "updated_at",
            "created_at"
        ]
        
    def resolve_thumbnail(self, info):
        return info.context.build_absolute_uri(self.thumbnail.url)
        
    def resolve_user(self, info):
        user = self.user        
        return {
            "first_name": user.first_name,
            "last_name": user.last_name,
            "username": user.username,
            "picture": user.picture.url if user.picture else ""
        }


    def resolve_tags(self, info):
        return [
            i.name
            for i in self.tags.all()
            if self.tags is not None
        ]
        

class Query(graphene.ObjectType):
    article = graphene.Field(ArticleNode, slug=graphene.String())
    articles = DjangoFilterConnectionField(ArticleNode)
    
    def resolve_article(self, info, slug):
        return get_object_or_404(Article, slug=slug)
    
    def resolve_articles(self, info, *args, **kwargs):
        return Article.objects.all().order_by("-updated_at")
    
    
schema = graphene.Schema(query=Query)
