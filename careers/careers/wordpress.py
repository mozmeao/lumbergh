import bleach
import requests


def _request(api_url, limit=None, page=1):
    # 100 is max per page from WP
    per_page = limit or 100
    resp = requests.get(api_url, params={'per_page': per_page, 'page': page}, timeout=5)
    resp.raise_for_status()
    data = resp.json()
    if limit is None and page == 1:
        num_pages = int(resp.headers.get('x-wp-totalpages', 1))
        if num_pages > 1:
            for i in range(2, num_pages + 1):
                data.extend(_request(api_url, page=i))

    return data


def _api_url(data_type, data_id):
    api_url = 'https://blog.mozilla.org/careers/wp-json/wp/v2/{}/'.format(data_type)
    if data_id:
        api_url += str(data_id)
    return api_url


def get_wp_data(data_type, data_id=None, limit=None):
    try:
        if data_type == 'posts' and limit is None:
            limit = 2

        api_url = _api_url(data_type, data_id)

        if data_id:
            data = _request(api_url, limit=1)
        else:
            data = _request(api_url, limit=limit)

        return data
    except Exception:
        return None


def get_posts_data(num_posts=None):
    posts = get_wp_data('posts', limit=num_posts)
    if not posts:
        return None

    return posts


def complete_posts_data(posts):
    # posts will be a list of tuples (db obj or None, post data dict)
    tags = get_feed_tags()
    for post in posts:
        post['tags'] = [tags[t] for t in post['tags']]
        update_post_media(post)


def get_feed_tags():
    tags = get_wp_data('tags')
    return {t['id']: t['slug'] for t in tags}


def update_post_media(post):
    """Fill out posts with featured media info"""
    # some blogs set featured_media to 0 when none is set
    if 'featured_media' in post:
        if post['featured_media']:
            media = get_wp_data('media', post['featured_media'])
            if media:
                post['featured_media'] = media
                return

        # blank featured_media value if anything went wrong
        post['featured_media'] = {}


def strip_tags(text):
    return bleach.clean(text, tags=[], strip=True).strip()


def process_excerpt(excerpt):
    summary = strip_tags(excerpt)
    if summary.lower().endswith('continue reading'):
        summary = summary[:-16]

    if summary.lower().endswith('read more'):
        summary = summary[:-9]

    if summary.lower().endswith('[&hellip;]'):
        summary = summary[:-10] + '…'

    if summary.endswith('[…]'):
        summary = summary[:-3] + '…'

    return summary
