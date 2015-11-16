from django import forms

import utils


class PositionFilterForm(forms.Form):
    team = forms.ChoiceField(widget=forms.Select(attrs={'autocomplete': 'off'}))
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
        types = utils.get_all_position_types()
        self.fields['position_type'].choices = [('', 'All Positions')] + [(k, k) for k in types]

        categories = utils.get_all_categories()
        self.fields['team'].choices = [('', 'All Categories')] + [(k, k) for k in categories]
