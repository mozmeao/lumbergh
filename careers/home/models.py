from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel

class HomeIndexPage(Page):
    heroHeader = models.CharField(max_length=255)
    heroText = models.CharField(max_length=255)
    applyButtonUrl = models.CharField(max_length=255)
    applyButtonText = models.CharField(max_length=255)

    videoUrlCode = models.CharField(max_length=255)
    dataOneA = models.CharField(max_length=255)
    dataOneB = models.CharField(max_length=255)
    dataOneC = models.CharField(max_length=255)
    leadOneTitle = RichTextField(blank=True)
    leadOneContent = RichTextField(blank=True)
    SurveyContentTitle = RichTextField(blank=True)
    SurveyContentContent = RichTextField(blank=True)
    ContentBlockOneVideoId = models.CharField(max_length=255)
    ContentBlockOneTitle = RichTextField(blank=True)
    ContentBlockOneContent = RichTextField(blank=True)

    imageA = models.ForeignKey(
        'wagtailimages.Image', 
        related_name='+',
        on_delete=models.SET_NULL,
        null=True
    )

    imageB = models.ForeignKey(
        'wagtailimages.Image', 
        related_name='+',
        on_delete=models.SET_NULL,
        null=True
    )

    imageC = models.ForeignKey(
        'wagtailimages.Image',
        related_name='+',
        on_delete=models.SET_NULL,
        null=True
    )

    imageD = models.ForeignKey(
        'wagtailimages.Image', 
        related_name='+',
        on_delete=models.SET_NULL,
        null=True
    )

    imageE = models.ForeignKey(
        'wagtailimages.Image', 
        related_name='+',
        on_delete=models.SET_NULL,
        null=True
    )

    imageF = models.ForeignKey(
        'wagtailimages.Image', 
        related_name='+',
        on_delete=models.SET_NULL,
        null=True
    )

    content_panels = Page.content_panels + [
        FieldPanel('heroHeader'),
        FieldPanel('heroText'),

        FieldPanel('videoUrlCode'),
        FieldPanel('applyButtonUrl'),
        FieldPanel('applyButtonText'),
        FieldPanel('dataOneA'),
        FieldPanel('dataOneB'),
        FieldPanel('dataOneC'),
        FieldPanel('leadOneTitle'),
        FieldPanel('leadOneContent'),
        FieldPanel('SurveyContentTitle'),
        FieldPanel('SurveyContentContent'),
        FieldPanel('ContentBlockOneVideoId'),
        FieldPanel('ContentBlockOneTitle'),
        FieldPanel('ContentBlockOneContent'),
        ImageChooserPanel('imageA'),
        ImageChooserPanel('imageB'),
        ImageChooserPanel('imageC'),
        ImageChooserPanel('imageD'),
        ImageChooserPanel('imageE'),
        ImageChooserPanel('imageF'),
    ]
