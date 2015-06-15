from django.core.urlresolvers import reverse
from django.db import models
from django.template.defaultfilters import slugify


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)


class Position(models.Model):
    shortcode = models.CharField(max_length=25)
    title = models.CharField(max_length=100)
    category = models.ForeignKey(Category, null=True, blank=True)
    job_type = models.CharField(max_length=255)
    location = models.CharField(max_length=150, null=True, blank=True)
    detail_url = models.URLField()
    apply_url = models.URLField()
    description = models.TextField()

    def __str__(self):
        return self.shortcode

    @property
    def location_filter(self):
        return self.location

    def get_absolute_url(self):
        return reverse('careers.workable_position', kwargs={'shortcode': self.shortcode})
