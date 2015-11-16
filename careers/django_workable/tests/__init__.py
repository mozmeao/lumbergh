import factory
from factory import fuzzy

from .. import models


class CategoryFactory(factory.DjangoModelFactory):
    FACTORY_FOR = models.Category
    name = factory.Sequence(lambda n: 'category {0}'.format(n))
    slug = factory.Sequence(lambda n: 'category-{0}'.format(n))


class PositionFactory(factory.DjangoModelFactory):
    FACTORY_FOR = models.Position
    shortcode = factory.Sequence(lambda n: 'shortcode{0}'.format(n))
    category = factory.SubFactory(CategoryFactory)
    title = factory.Sequence(lambda n: 'Job Title {0}'.format(n))
    job_type = fuzzy.FuzzyChoice(['Full-Time', 'Part-Time', 'Contractor', 'Intern'])
    location = fuzzy.FuzzyChoice(['Mountain View', 'San Francisco', 'Remote', 'Toronto'])
    description = factory.Sequence(lambda n: 'Job Description {0}'.format(n))

    @factory.lazy_attribute
    def apply_url(self):
        url = 'https://mofo.workable.com/jobs/{0}/candidates/new'
        return url.format(self.shortcode)

    @factory.lazy_attribute
    def detail_url(self):
        url = 'https://mofo.workable.com/j/{0}'
        return url.format(self.shortcode)
