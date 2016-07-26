from django.conf import settings

import factory
from factory import fuzzy

from careers.careers.models import Position


class PositionFactory(factory.DjangoModelFactory):
    FACTORY_FOR = Position
    job_id = factory.Sequence(lambda n: 'jobid{0}'.format(n))
    title = factory.Sequence(lambda n: 'Job Title {0}'.format(n))
    department = fuzzy.FuzzyChoice(['Data Analytics', 'Engineering'])
    location = fuzzy.FuzzyChoice(['Mountain View', 'San Francisco', 'Remote', 'Toronto'])
    description = factory.Sequence(lambda n: 'Job Description {0}'.format(n))
    source = 'gh'
    position_type = fuzzy.FuzzyChoice(['Full-Time', 'Part-Time', 'Contractor', 'Intern'])

    @factory.lazy_attribute
    def apply_url(self):
        if self.source == 'gh':
            url = 'https://boards.greenhouse.io/{}/jobs/{}'.format(
                settings.GREENHOUSE_BOARD_TOKEN,
                self.job_id)
            return url.format(self.job_id)
