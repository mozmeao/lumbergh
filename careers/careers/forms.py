from django import forms

from django_jobvite.models import Category


class PositionFilterForm(forms.Form):
    team = forms.ModelChoiceField(queryset=Category.objects.order_by('name'),
                                  empty_label='All Positions',
                                  widget=forms.Select(attrs={'autocomplete': 'off'}))
    position_type = forms.ChoiceField(choices=(
        ('', 'All Positions'),
        ('Full time', 'Full time'),
        ('Contractor', 'Contractor'),
        ('Intern', 'Intern'),
    ), widget=forms.Select(attrs={'autocomplete': 'off'}))
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
