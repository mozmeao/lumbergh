from django import forms

from django_jobvite.models import Category, Position


class PositionFilterForm(forms.Form):
    team = forms.ModelChoiceField(queryset=Category.objects.order_by('name'),
                                  empty_label='All Teams',
                                  widget=forms.Select(attrs={'autocomplete': 'off'}))
    position_type = forms.ChoiceField(widget=forms.Select(attrs={'autocomplete': 'off'}))
    location = forms.ChoiceField(choices=(
        ('', 'All Locations'),
        ('remote', 'Remote'),

        # Continents
        ('europe', 'Europe'),
        ('latinamerica', 'Latin America'),
        ('northamerica', 'North America'),

        # Young money
        ('bayarea', 'Bay Area'),

        # Cities
        ('berlin', 'Berlin'),
        ('boston', 'Boston'),
        ('london', 'London'),
        ('mountainview', 'Mountain View'),
        ('newzealand', 'New Zealand'),
        ('paris', 'Paris'),
        ('portland', 'Portland'),
        ('sanfrancisco', 'San Francisco'),
        ('toronto', 'Toronto'),
        ('vancouver', 'Vancouver'),
    ), widget=forms.Select(attrs={'autocomplete': 'off'}))

    def __init__(self, *args, **kwargs):
        super(PositionFilterForm, self).__init__(*args, **kwargs)

        # Populate position type choices dynamically.
        types = Position.objects.values_list('job_type', flat=True).distinct().order_by('job_type')
        self.fields['position_type'].choices = [('', 'All Positions')] + [(k, k) for k in types]
