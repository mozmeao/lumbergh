from careers.base.tests import TestCase
from unittest.mock import patch

from careers.careers import wordpress


@patch.object(wordpress, 'requests')
class TestAPI(TestCase):
    def test_request(self, req_mock):
        wordpress.get_wp_data('posts')
        req_mock.get.assert_called_once_with(
            'https://blog.mozilla.org/careers/wp-json/wp/v2/posts/',
            params={'per_page': 100, 'page': 1},
            timeout=5)

    def test_request_with_data_id(self, req_mock):
        wordpress.get_wp_data('media', 12345)
        req_mock.get.assert_called_once_with(
            'https://blog.mozilla.org/careers/wp-json/wp/v2/media/12345',
            params={'per_page': 1, 'page': 1},
            timeout=5)


class TestGetFeaturedPost(TestCase):
    def setUp(self):
        self.posts_json = [
            {
                'id': 12345,
                'tags': ['foo', 'bar', 'baz'],
            },
            {
                'id': 12346,
                'tags': ['foo', 'bar', 'baz', 'story'],
            },
            {
                'id': 12347,
                'tags': [],
            },
            {
                'id': 12348,
                'tags': ['story', 'allegory', 'montessori']
            }
        ]

    def test_has_featued_post(self):
        posts_data, featured_post_data = wordpress.get_featured_post(self.posts_json)

        self.assertEqual(len(posts_data), 3)
        self.assertEqual(featured_post_data, {'id': 12346, 'tags': ['foo', 'bar', 'baz', 'story']})

    def test_no_featured_posts(self):
        self.posts_json[1]['tags'].remove('story')
        self.posts_json[3]['tags'].remove('story')

        posts_data, featured_post_data = wordpress.get_featured_post(self.posts_json)
        self.assertEqual(len(posts_data), 4)
        self.assertEqual(featured_post_data, None)


@patch.object(wordpress, 'get_posts_data')
@patch.object(wordpress, 'prepare_post_data')
@patch.object(wordpress, 'complete_posts_data')
class TestGetPosts(TestCase):
    def setUp(self):
        self.posts_json = [
            {
                'id': 12345,
                'tags': ['foo', 'bar', 'baz'],
            },
            {
                'id': 12346,
                'tags': ['foo', 'bar', 'baz', 'story'],
            },
            {
                'id': 12347,
                'tags': [],
            },
            {
                'id': 12348,
                'tags': ['story', 'allegory', 'montessori']
            }
        ]

    def test_no_posts_data(self, cpd_mock, ppd_mock, gpd_mock):
        gpd_mock.return_value = None

        featured_post, recent_posts = wordpress.get_posts()
        cpd_mock.assert_not_called()
        ppd_mock.assert_not_called()
        self.assertEqual(featured_post, None)
        self.assertEqual(recent_posts, None)

    def test_no_featured_post(self, cpd_mock, ppd_mock, gpd_mock):
        self.posts_json[1]['tags'].remove('story')
        self.posts_json[3]['tags'].remove('story')

        gpd_mock.return_value = self.posts_json
        ppd_mock.return_value = {}

        featured_post, recent_posts = wordpress.get_posts()

        cpd_mock.assert_called_once()
        self.assertEqual(ppd_mock.call_count, 3)
        self.assertEqual(featured_post, None)
        self.assertEqual(len(recent_posts), 3)

    def test_with_featured_post(self, cpd_mock, ppd_mock, gpd_mock):
        gpd_mock.return_value = self.posts_json
        ppd_mock.return_value = {}

        featured_post, recent_posts = wordpress.get_posts()

        cpd_mock.assert_called_once()
        self.assertEqual(ppd_mock.call_count, 3)
        self.assertNotEqual(featured_post, None)
        self.assertEqual(len(recent_posts), 2)
