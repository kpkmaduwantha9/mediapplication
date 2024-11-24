from django.test import TestCase, Client
from django.urls import reverse


class MedishopViewsTest(TestCase):
    """
    Tests for the Medishop application views.
    """

    def setUp(self):
        """
        Set up the test client and URLs.
        """
        self.client = Client()
        self.home_url = reverse('home')  # Make sure 'home' is the name of the URL pattern

    def test_home_view_status_code(self):
        """
        Test that the home view returns a status code of 200.
        """
        response = self.client.get(self.home_url)
        self.assertEqual(response.status_code, 200)

    def test_home_view_template_used(self):
        """
        Test that the home view renders the correct template.
        """
        response = self.client.get(self.home_url)
        self.assertTemplateUsed(response, 'home.html')
