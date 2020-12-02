from django.db import models

# Create your models here.
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel
from wagtail.core.fields import RichTextField
from wagtail.core.models import Page
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.snippets.models import register_snippet


class ProjectsPage(Page):
    subtitle = models.CharField(max_length=40)
    banner_image = models.ForeignKey(
        "wagtailimages.Image",
        blank=False,
        null=True,
        on_delete=models.SET_NULL
    )

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context["projects"] = Project.objects.all()
        return context

    content_panels = Page.content_panels + [
        FieldPanel("subtitle"),
        ImageChooserPanel("banner_image")
    ]


@register_snippet
class Project(models.Model):
    """The main menu clusterable model"""
    year = models.IntegerField()
    title = models.CharField(max_length=100)
    description = RichTextField()
    role = models.CharField(max_length=40)
    location = models.CharField(max_length=40)
    image = models.ForeignKey(
        "wagtailimages.Image",
        blank=False,
        null=True,
        on_delete=models.SET_NULL)

    panels = [
        MultiFieldPanel([
            FieldPanel("year"),
            FieldPanel("title"),
            FieldPanel("description"),
            FieldPanel("role"),
            FieldPanel("location"),
            ImageChooserPanel("image")
        ], heading="Projects"),
    ]

    def __str__(self):
        return self.title
