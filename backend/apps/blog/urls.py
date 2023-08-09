from django.urls import path
from .feeds import ArticleFeed


urlpatterns = [
    path(
        route="rss/",
        view=ArticleFeed(),
        name="article_feed"
    )
]