from datetime import date

import factory
from factory import fuzzy

from careers.university import models


class EventFactory(factory.DjangoModelFactory):
    FACTORY_FOR = models.Event
    name = factory.Sequence(lambda n: 'Test Event {0}'.format(n))
    location = factory.Sequence(lambda n: 'Test Location {0}'.format(n))
    start_date = fuzzy.FuzzyDate(date(2010, 1, 1))
    end_date = None
