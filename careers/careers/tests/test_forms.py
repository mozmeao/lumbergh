from careers.base.tests import TestCase
from careers.careers.forms import PositionFilterForm
from careers.careers.tests import PositionFactory as JobvitePositionFactory


class PositionFilterFormTests(TestCase):
    def test_dynamic_position_type_choices(self):
        """
        The choices for the position_type field should be dynamically
        generated from the available values in the database.
        """
        JobvitePositionFactory.create(job_type='Foo')
        JobvitePositionFactory.create(job_type='Bar')
        JobvitePositionFactory.create(job_type='Baz')
        JobvitePositionFactory.create(job_type='Foo')

        form = PositionFilterForm()
        self.assertEqual(form.fields['position_type'].choices, [
            ('', 'All Positions'),
            ('Bar', 'Bar'),  # Alphabetical order
            ('Baz', 'Baz'),
            ('Foo', 'Foo'),
        ])
