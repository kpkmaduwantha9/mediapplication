from django.test import TestCase, Client
from django.urls import reverse
from .models import Medicine
from datetime import date
from .forms import MedicineForm
# Create your tests here.


class MedicineModelTest(TestCase):
    """
    Basic tests for the Medicine model.
    """

    def setUp(self):
        """
        Set up a sample Medicine object for testing.
        """
        self.medicine = Medicine.objects.create(
            name="Paracetamol",
            description="Used to treat pain and fever.",
            price=50.00,
            stock=100,
            mfg_date=date(2023, 1, 1),
            expiry_date=date(2025, 1, 1)
        )

    def test_medicine_creation(self):
        """
        Test that a Medicine object can be created and its fields are stored correctly.
        """
        self.assertEqual(self.medicine.name, "Paracetamol")
        self.assertEqual(self.medicine.price, 50.00)
        self.assertEqual(self.medicine.stock, 100)
        self.assertEqual(self.medicine.mfg_date, date(2023, 1, 1))
        self.assertEqual(self.medicine.expiry_date, date(2025, 1, 1))

    def test_str_representation(self):
        """
        Test the string representation of a Medicine object.
        """
        self.assertEqual(str(self.medicine), "Paracetamol")



class MedicineViewsTest(TestCase):
    """
    Tests for the Medicine application views.
    """

    def setUp(self):
        """
        Set up initial data for testing.
        """
        self.client = Client()
        self.medicine = Medicine.objects.create(
            name="Paracetamol",
            description="Used to treat pain and fever.",
            price=50.00,
            stock=100,
            mfg_date=date(2023, 1, 1),
            expiry_date=date(2025, 1, 1),
        )
        self.medicine_home_url = reverse('medicine_home')
        self.add_medicine_url = reverse('add_medicine')
        self.edit_medicine_url = reverse('edit_medicine', args=[self.medicine.id])
        self.delete_medicine_url = reverse('delete_medicine', args=[self.medicine.id])

    def test_medicine_home_view(self):
        """
        Test if the medicine_home view renders correctly.
        """
        response = self.client.get(self.medicine_home_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'medicine/medicine_home.html')

    def test_add_medicine_view_get(self):
        """
        Test the GET request to add_medicine view.
        """
        response = self.client.get(self.add_medicine_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'medicine/add_medicine.html')

    def test_add_medicine_view_post_valid(self):
        """
        Test the POST request to add_medicine view with valid data.
        """
        response = self.client.post(self.add_medicine_url, {
            'name': 'Aspirin',
            'description': 'Used to reduce pain, fever, or inflammation.',
            'price': 25.00,
            'stock': 50,
            'mfg_date': '2023-02-01',
            'expiry_date': '2025-02-01',
        })
        self.assertEqual(response.status_code, 302)  # Redirect after successful form submission
        self.assertEqual(Medicine.objects.count(), 2)  # Check if a new medicine was added

    def test_edit_medicine_view_get(self):
        """
        Test the GET request to edit_medicine view.
        """
        response = self.client.get(self.edit_medicine_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'medicine/edit_medicine.html')

    def test_edit_medicine_view_post_valid(self):
        """
        Test the POST request to edit_medicine view with valid data.
        """
        response = self.client.post(self.edit_medicine_url, {
            'name': 'Updated Paracetamol',
            'description': 'Updated description.',
            'price': 60.00,
            'stock': 80,
            'mfg_date': '2023-01-01',
            'expiry_date': '2025-01-01',
        })
        self.assertEqual(response.status_code, 302)  # Redirect after successful form submission
        self.medicine.refresh_from_db()
        self.assertEqual(self.medicine.name, 'Updated Paracetamol')  # Check if the name was updated

    def test_delete_medicine_view(self):
        """
        Test the delete_medicine view.
        """
        response = self.client.post(self.delete_medicine_url)
        self.assertEqual(response.status_code, 302)  # Redirect after successful deletion
        self.assertEqual(Medicine.objects.count(), 0)  # Check if the medicine was deleted
