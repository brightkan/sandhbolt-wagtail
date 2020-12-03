from django.db import models

# Create your models here.
from wagtail.admin.edit_handlers import RichTextFieldPanel, FieldPanel, MultiFieldPanel
from wagtail.core.models import Page
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.snippets.models import register_snippet


class GalleryPage(Page):
    subtitle = models.CharField(max_length=40)
    banner_image = models.ForeignKey(
        "wagtailimages.Image",
        blank=False,
        null=True,
        on_delete=models.SET_NULL
    )

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context["gallery_images"] = GalleryImage.objects.all()
        return context

    content_panels = Page.content_panels + [
        FieldPanel("subtitle"),
        ImageChooserPanel("banner_image")
    ]


@register_snippet
class GalleryImage(models.Model):
    caption = models.CharField(max_length=40)
    image = models.ForeignKey(
        "wagtailimages.Image",
        blank=False,
        null=True,
        on_delete=models.CASCADE)

    width = models.IntegerField()
    height = models.IntegerField()

    panels = [
        MultiFieldPanel([
            FieldPanel("caption"),
            ImageChooserPanel("image"),
            FieldPanel("width"),
            FieldPanel("height"),
        ], heading="Gallery Images"),
    ]

    def __str__(self):
        return self.caption
