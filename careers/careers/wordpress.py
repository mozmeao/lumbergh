# this file is a simplified version of the wordpress app in bedrock
# https://github.com/mozilla/bedrock/tree/master/bedrock/wordpress

import bleach
import requests

from django.conf import settings
from jinja2 import Markup


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


def get_featured_post(posts_data):
    featured_post_data = None
    featured_post_index = None

    for idx, post in enumerate(posts_data):
        if 'story' in post['tags']:
            featured_post_data = post
            featured_post_index = idx
            break

    if featured_post_index:
        del posts_data[featured_post_index]

    return posts_data, featured_post_data


def prepare_post_data(post_data):
    # sometimes a post doesn't have a `post-large` image
    try:
        image = post_data['featured_media']['media_details']['sizes']['post-large']['source_url']  # noqa
    except Exception:
        image = None

    return {
        'title': Markup(post_data['title']['rendered']).unescape(),
        'link': post_data['link'],
        'excerpt': Markup(process_excerpt(post_data['excerpt']['rendered'])),
        'image': image,
    }


def get_posts():
    # blog content isn't critical to the page. if the wordpress API fails
    # for some reason, we can just move on and wait for the next build
    try:
        # 100 posts should give us over a year of content in which to find
        # a featured/tagged post
        posts_data = get_posts_data(num_posts=100)
    except Exception:
        posts_data = None

    if posts_data:
        complete_posts_data(posts_data)

        posts, featured_post_data = get_featured_post(posts_data)

        if featured_post_data:
            featured_post = prepare_post_data(featured_post_data)
            recent_posts_data = posts[:2]
        else:
            # we always want to show 3 posts, so if a featured post wasn't
            # found, grab the 3 latest posts
            featured_post = None
            recent_posts_data = posts[:3]

        recent_posts = [prepare_post_data(post) for post in recent_posts_data]

        # notify dms when blog posts are successfully fetched
        if settings.DMS_BLOG_FETCH:
            requests.get(settings.DMS_BLOG_FETCH)
    else:
        featured_post = None
        recent_posts = None

    return featured_post, recent_posts
