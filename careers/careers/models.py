from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Position(models.Model):
    job_id = models.CharField(max_length=10)
    title = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    description = models.TextField()
    apply_url = models.URLField()
    source = models.CharField(max_length=100)

    def __str__(self):
        return '{}@{}'.format(self.job_id, self.source)
