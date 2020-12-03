from django.db import models
from wagtail.admin.edit_handlers import FieldPanel, RichTextFieldPanel, MultiFieldPanel
from wagtail.core.models import Page
from wagtail.images.edit_handlers import ImageChooserPanel


class HomePage(Page):
    company_description = models.TextField()
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

    panels = [
        MultiFieldPanel([
            FieldPanel("sub_title"),
            FieldPanel("title"),
            ImageChooserPanel("image")
        ], heading="sliders"), ]

    def __str__(self):
        return f'{self.sub_title}'
