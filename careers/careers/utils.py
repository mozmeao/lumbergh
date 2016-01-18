from itertools import chain

from django_jobvite import models as jobvite_models
from careers.django_workable import models as workable_models


def get_all_positions(filters=None, order_by=None):
    if not filters:
        filters = {}

    if not order_by:
        def order_by_function(x):
            return x.title
        order_by = order_by_function

    return (
        sorted(
            chain(workable_models.Position.objects.filter(**filters),
                  jobvite_models.Position.objects.filter(**filters)),
            key=order_by))


def get_all_categories():
    return (
        sorted(set(
            chain(jobvite_models.Category.objects.values_list('name', flat=True),
                  workable_models.Category.objects.values_list('name', flat=True)))))


def get_all_position_types():
    return (
        sorted(set(
            chain(jobvite_models.Position.objects.values_list('job_type', flat=True),
                  workable_models.Position.objects.values_list('job_type', flat=True)))))
