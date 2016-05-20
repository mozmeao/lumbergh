from careers.base.tests import TestCase
from careers.careers import utils
from careers.careers.tests import (CategoryFactory as JobviteCategoryFactory,
                                   PositionFactory as JobvitePositionFactory)


class GetAllPositionsTests(TestCase):
    def test_base(self):
        jobvite_1 = JobvitePositionFactory.create(title='Abc')
        jobvite_2 = JobvitePositionFactory.create(title='Def')

        positions = utils.get_all_positions()
        self.assertEqual(positions, [jobvite_1, jobvite_2])

    def test_filters(self):
        jobvite_1 = JobvitePositionFactory.create(title='aaa')
        JobvitePositionFactory.create(title='bbb')

        positions = utils.get_all_positions(filters={'title__contains': 'aaa'})
        self.assertEqual(set(positions), set([jobvite_1]))

    def test_orderby(self):
        jobvite_1 = JobvitePositionFactory.create(title='aaa', location='b')
        jobvite_2 = JobvitePositionFactory.create(title='ccc', location='a')

        positions = utils.get_all_positions(order_by=lambda x: x.location)
        self.assertEqual(positions, [jobvite_2, jobvite_1])


class GetAllCategoriesTests(TestCase):
    def test_base(self):
        jobvite_1 = JobviteCategoryFactory.create(name='ccc')
        jobvite_2 = JobviteCategoryFactory.create(name='aaa')

        categories = utils.get_all_categories()
        self.assertEqual(categories, [jobvite_2.name, jobvite_1.name])


class GetAllPositionTypesTests(TestCase):
    def test_base(self):
        JobvitePositionFactory.create(job_type='aaa')
        JobvitePositionFactory.create(job_type='bbb')

        job_types = utils.get_all_position_types()
        self.assertEqual(job_types, ['aaa', 'bbb'])
