from django_jinja import library


@library.global_function
def format_event_date(event):
    start_date = event['start_date']
    end_date = event['end_date']

    if start_date == end_date:
        date_string = start_date.strftime('%b {start.day}, %Y')
    elif start_date.month == end_date.month:
        date_string = start_date.strftime('%b {start.day}-{end.day}, %Y')
    else:
        date_string = '{0} - {1}'.format(
            start_date.strftime('%b {start.day}, %Y'),
            end_date.strftime('%b {end.day}, %Y')
        )

    # We use string formatting to insert the day to avoid 0 padding.
    return date_string.format(start=start_date, end=end_date)
