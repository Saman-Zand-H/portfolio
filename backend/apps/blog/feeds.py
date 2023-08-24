from django.db.models.base import Model
from django.utils import timezone
from django.template.defaultfilters import truncatewords
from django.contrib.syndication.views import Feed
from django.utils.feedgenerator import Rss201rev2Feed

from .utils import CommonMarkdown
from .models import Article


class CustomRSS(Rss201rev2Feed):
    content_type = "application/xml"


class ArticleFeed(Feed):
    title = "SamanZND"
    link = "/blog/"
    description = "Latest articles from my blog"
    feed_type = CustomRSS

    def items(self):
        return (
            Article.objects.prefetch_related("tags").all().order_by("-updated_at")[:20]
        )

    def item_title(self, item):
        return item.title.title()

    def item_pubdate(self, item):
        return item.created_at

    def item_updateddate(self, item):
        return item.updated_at

    def author_name(self):
        return "Saman Zand"

    def item_description(self, item):
        return truncatewords(CommonMarkdown.get_markdown(item.article), 40)

    def item_content(self, item):
        return item.item

    def feed_copyright(self):
        return f"Copyright©{timezone.now().year}"

    def item_link(self, item):
        return f"https://samanznd.ir/blog/{item.slug}"

    def item_guid(self, item):
        return item.slug
