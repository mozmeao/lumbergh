from mock import patch
from nose.tools import eq_

from careers.base.tests import TestCase
from careers.careers import utils
from careers.careers.tests import (CategoryFactory as JobviteCategoryFactory,
                                   PositionFactory as JobvitePositionFactory)
from careers.django_workable.tests import (CategoryFactory as WorkableCategoryFactory,
                                           PositionFactory as WorkablePositionFactory)


class GetAllPositionsTests(TestCase):
    def test_base(self):
        jobvite_1 = JobvitePositionFactory.create(title='Abc')
        jobvite_2 = JobvitePositionFactory.create(title='Def')
        workable_1 = WorkablePositionFactory.create(title='Bcd')

        positions = utils.get_all_positions()
        eq_(positions, [jobvite_1, workable_1, jobvite_2])

    def test_filters(self):
        jobvite_1 = JobvitePositionFactory.create(title='aaa')
        jobvite_2 = JobvitePositionFactory.create(title='bbb')
        workable_1 = WorkablePositionFactory.create(title='aaa')

        positions = utils.get_all_positions(filters={'title__contains': 'aaa'})
        eq_(positions, [jobvite_1, workable_1])

    def test_orderby(self):
        jobvite_1 = JobvitePositionFactory.create(title='aaa', location='b')
        workable_1 = WorkablePositionFactory.create(title='bbb', location='c')
        jobvite_2 = JobvitePositionFactory.create(title='ccc', location='a')

        positions = utils.get_all_positions(order_by=lambda x: x.location)
        eq_(positions, [jobvite_2, jobvite_1, workable_1])


class GetAllCategoriesTests(TestCase):
    def test_base(self):
        jobvite_1 = JobviteCategoryFactory.create(name='ccc')
        workable_1 = WorkableCategoryFactory.create(name='bbb')
        jobvite_2 = JobviteCategoryFactory.create(name='aaa')

        categories = utils.get_all_categories()
        eq_(categories, [jobvite_2.name, workable_1.name, jobvite_1.name])


class GetAllPositionTypesTests(TestCase):
    def test_base(self):
        jobvite_1 = JobvitePositionFactory.create(job_type='aaa')
        workable_1 = WorkablePositionFactory.create(job_type='aaa')
        jobvite_2 = JobvitePositionFactory.create(job_type='bbb')

        job_types = utils.get_all_position_types()
        eq_(job_types, ['aaa', 'bbb'])
