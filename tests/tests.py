from django.test import TestCase
from django.test.client import Client


class TestNavTemplatetag(TestCase):
    def setUp(self):
        self.client = Client()

    def test_nav_home(self):
        # Issue a GET request to the Home page.
        response = self.client.get('/')

        # Check that the response is 200 OK.
        self.failUnlessEqual(response.status_code, 200)

        # Check that the home.html template is being used.
        self.assertTemplateUsed(response, 'home.html')

        # Check that the home page is 'selected'.
        self.assertContains(
            response,
            '<li class="selected"><a href="/" rel="home" accesskey="1">Home'
            '</a></li>'
        )

        # Check that the about page is not 'selected'.
        self.assertContains(
            response,
            '<li><a href="/about/">About</a></li>'
        )

    def test_nav_about(self):
        # Issue a GET request to the Home page.
        response = self.client.get('/about/')

        # Check that the response is 200 OK.
        self.failUnlessEqual(response.status_code, 200)

        # Check that the home.html template is being used.
        self.assertTemplateUsed(response, 'about.html')

        # Check that the home page is not 'selected'.
        self.assertContains(
            response,
            '<li><a href="/" rel="home" accesskey="1">Home</a></li>'
        )

        # Check that the about page is 'selected'.
        self.assertContains(
            response,
            '<li class="selected"><a href="/about/">About</a></li>'
        )


class TestStripQuerystringFilter(TestCase):
    def setUp(self):
        self.client = Client()

    def test_strip_querystring_filter(self):
        # Issue a GET request to the Home page.
        response = self.client.get('/strip-querystring-test/')

        # Check that the response is 200 OK.
        self.failUnlessEqual(response.status_code, 200)

        # Check that the home.html template is being used.
        self.assertTemplateUsed(response, 'strip_querystring_filter_test_template.html')

        # Check that the response contains what we expect.
        self.assertContains(
            response,
            'https://example.com/',
            count=2
        )

        # Check that the response doesn't contain what we don't want.
        self.assertNotContains(
            response,
            '?foo=bar&spam=eggs'
        )

        # Check that the response doesn't contain what we don't want.
        self.assertNotContains(
            response,
            '?product_id=1&variation=2&utm_source=The-WWW'
        )