def generate_position_meta_description(position):
    suffix = 'n' if position.position_type.lower().startswith(('a', 'e', 'i', 'o', 'u')) else ''
    meta = (
        f'Mozilla is hiring a{suffix} '
        f'{position.position_type.lower()} {position.title} in '
    )

    meta = meta + position.job_locations

    return meta
