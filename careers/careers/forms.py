from django import forms

from careers.careers.models import Position


class PositionFilterForm(forms.Form):
    team = forms.ChoiceField(widget=forms.Select(attrs={'autocomplete': 'off'}))
    position_type = forms.ChoiceField(widget=forms.Select(attrs={'autocomplete': 'off'}))
    location = forms.ChoiceField(widget=forms.Select(attrs={'autocomplete': 'off'}))

    def __init__(self, *args, **kwargs):
        super(PositionFilterForm, self).__init__(*args, **kwargs)

        # Populate position type choices dynamically.
        locations = Position.locations()
        if 'All Offices' in locations:
            locations.remove('All Offices')

        self.fields['location'].choices = (
            [('', 'All Locations')] + [(l, l) for l in locations])

        types = Position.position_types()
        self.fields['position_type'].choices = (
            [('', 'All Positions')] + [(t, t) for t in types])

        categories = Position.categories()
        self.fields['team'].choices = (
            [('', 'All Categories')] + [(k, k) for k in categories])
