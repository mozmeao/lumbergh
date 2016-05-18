from django_jobvite import models as jobvite_models


def get_all_positions(filters=None, order_by=None):
    if not filters:
        filters = {}

    if not order_by:
        def order_by_function(x):
            return x.title
        order_by = order_by_function

    return sorted(jobvite_models.Position.objects.filter(**filters), key=order_by)


def get_all_categories():
    return sorted(set(jobvite_models.Category.objects.values_list('name', flat=True)))


def get_all_position_types():
    return sorted(set(jobvite_models.Position.objects.values_list('job_type', flat=True)))
