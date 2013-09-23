from django.core.exceptions import ValidationError
from django.db import models


class Event(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True,
                                help_text='Leave blank if event is 1 day long.')

    @property
    def date(self):
        if not self.end_date:
            date_string = self.start_date.strftime('%b {start.day}, %Y')
        elif self.start_date.month == self.end_date.month:
            date_string = self.start_date.strftime('%b {start.day}-{end.day}, %Y')
        else:
            date_string = '{0} - {1}'.format(
                self.start_date.strftime('%b {start.day}, %Y'),
                self.end_date.strftime('%b {end.day}, %Y')
            )

        # We use string formatting to insert the day to avoid 0 padding.
        return date_string.format(start=self.start_date, end=self.end_date)

    def clean(self):
        if self.end_date and self.end_date <= self.start_date:
            raise ValidationError('An event\'s end date must occur after the start date.')

    def __unicode__(self):
        return u'{0}, {1} - {2}'.format(self.name, self.location, self.date)
