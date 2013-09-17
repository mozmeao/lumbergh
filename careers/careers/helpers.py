from jingo import register


JOB_TYPE_NAMES = {
    'Employee': 'Full time',
    'Seasonal': 'Contractor',
    'Intern': 'Intern'
}


@register.filter
def readable_job_type(job_type):
    return JOB_TYPE_NAMES.get(job_type, job_type)

