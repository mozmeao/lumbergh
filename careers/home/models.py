from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel


class HomePage(Page):
    heroHeader = RichTextField(blank=True)
    heroText = RichTextField(blank=True)
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

    content_panels = Page.content_panels + [
        FieldPanel('heroHeader', classname="full"),
        FieldPanel('heroText', classname="full"),
        FieldPanel('videoUrlCode', classname="full"),
        FieldPanel('dataOneA', classname="full"),
        FieldPanel('dataOneB', classname="full"),
        FieldPanel('dataOneC', classname="full"),
        FieldPanel('leadOneTitle', classname="full"),
        FieldPanel('leadOneContent', classname="full"),
        FieldPanel('SurveyContentTitle', classname="full"),
        FieldPanel('SurveyContentContent', classname="full"),
        FieldPanel('ContentBlockOneVideoId', classname="full"),
        FieldPanel('ContentBlockOneTitle', classname="full"),
        FieldPanel('ContentBlockOneContent', classname="full"),
    ]
