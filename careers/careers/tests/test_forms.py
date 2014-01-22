from nose.tools import eq_

from careers.base.tests import TestCase
from careers.careers.forms import PositionFilterForm
from careers.careers.tests import PositionFactory


class PositionFilterFormTests(TestCase):
    def test_dynamic_position_type_choices(self):
        """
        The choices for the position_type field should be dynamically
        generated from the available values in the database.
        """
        PositionFactory.create(job_type='Foo')
        PositionFactory.create(job_type='Bar')
        PositionFactory.create(job_type='Baz')
        PositionFactory.create(job_type='Foo')
        PositionFactory.create(job_type='Biff')

        form = PositionFilterForm()
        eq_(form.fields['position_type'].choices, [
            ('', 'All Positions'),
            ('Bar', 'Bar'),  # Alphabetical order
            ('Baz', 'Baz'),
            ('Biff', 'Biff'),
            ('Foo', 'Foo'),
        ])
