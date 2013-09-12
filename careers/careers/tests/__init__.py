from datetime import date

import factory
from django_jobvite.models import Category, Position
from factory import fuzzy


class FuzzyDateString(fuzzy.FuzzyDate):
    def fuzz(self):
        date = super(FuzzyDateString, self).fuzz()
        return date.strftime('%m/%d/%Y')


class CategoryFactory(factory.DjangoModelFactory):
    FACTORY_FOR = Category
    name = factory.Sequence(lambda n: 'category {0}'.format(n))
    slug = factory.Sequence(lambda n: 'category-{0}'.format(n))


class PositionFactory(factory.DjangoModelFactory):
    FACTORY_FOR = Position
    category = factory.SubFactory(CategoryFactory)
    job_id = factory.Sequence(lambda n: 'jobid{0}'.format(n))
    title = factory.Sequence(lambda n: 'Job Title {0}'.format(n))
    job_type = fuzzy.FuzzyChoice(['Full-Time', 'Part-Time', 'Contractor', 'Intern'])
    requisition_id = fuzzy.FuzzyInteger(0)
    location = fuzzy.FuzzyChoice(['Mountain View', 'San Francisco', 'Remote', 'Toronto'])
    date = FuzzyDateString(date(2010, 1, 1))
    description = factory.Sequence(lambda n: 'Job Description {0}'.format(n))

    @factory.lazy_attribute
    def apply_url(self):
        url = 'http://hire.jobvite.com/CompanyJobs/Apply.aspx?c=qpX9Vfwaj&j={0}'
        return url.format(self.job_id)

    @factory.lazy_attribute
    def detail_url(self):
        return 'http://hire.jobvite.com/CompanyJobs/Job.aspx?c=qpX9Vfwaj&j={0}'.format(self.job_id)
