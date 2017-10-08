from django.test import TestCase
from django.urls import resolve
from lists.views import home_page
from django.http import HttpRequest

# Create your tests here.


class HomePageTest(TestCase):

	def test_root_url_resolves_to_homepage_view(self):
		found = resolve('/')
		self.assertEquals(found.func, home_page)

	def test_home_page_view_returns_correct_html(self):
		request = HttpRequest()
		print('The default method for HttpRequest is: '+str(request.method))
		response = home_page(request)
		html = response.content.decode('utf8')
		self.assertTrue(html.startswith('<html>'))
		self.assertIn('<title>To-Do lists</title>',html)
		self.assertTrue(html.endswith('</html>'))

