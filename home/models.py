from django.db import models
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel, RichTextFieldPanel
from wagtail.core import blocks

from wagtail.core.fields import StreamField

from wagtail.core.models import Page


class HomePage(Page):
    """Context"""
    company_description =models.TextField()
    vision = models.TextField()
    mission = models.TextField()

    content_panels = Page.content_panels + [
        RichTextFieldPanel("company_description"),
        RichTextFieldPanel("vision"),
        RichTextFieldPanel("mission"),
    ]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context["sliders"] = Slider.objects.all()
        return context


class Slider(models.Model):
    sub_title = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    image = models.ForeignKey(
        "wagtailimages.Image",
        blank=False,
        null=True,
        on_delete=models.SET_NULL
    )

    def __str__(self):
        return f'{self.sub_title}'
