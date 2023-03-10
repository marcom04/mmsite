from django.db import models

from wagtail.models import Page
from wagtail.admin.panels import FieldPanel, StreamFieldPanel
from wagtail.core.fields import StreamField

from streams import blocks


class FlexPage(Page):
    template = "flex/flex_page.html"

    content = StreamField(
        [
            ("title_and_text", blocks.TitleAndTextBlock()),
            ("full_richtext", blocks.RichTextBlock()),
            ("simple_richtext", blocks.SimpleRichTextBlock()),
            ("cards", blocks.CardBlock()),
        ],
        null=True, blank=True
    )

    subtitle = models.CharField(max_length=100, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("subtitle"),
        StreamFieldPanel("content"),
    ]

    class Meta:
        verbose_name = "Flex Page"
        verbose_name_plural = "Flex Pages"
