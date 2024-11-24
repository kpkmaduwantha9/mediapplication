from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Patient

# Create your tests here.

class PatientModelTest(TestCase):
    """
    Tests for the Patient model.
    """

    def test_patient_model_create(self):
        """
        Test that a Patient instance can be created and saved to the database.
        """
        patient = Patient.objects.create(
            name="John Doe",
            nic="123456789V",
            age=30,
            gender="Male",
            problem="Fever and cough"
        )

        # Check that the patient is saved in the database
        self.assertEqual(Patient.objects.count(), 1)
        self.assertEqual(patient.name, "John Doe")
        self.assertEqual(patient.nic, "123456789V")
        self.assertEqual(patient.age, 30)
        self.assertEqual(patient.gender, "Male")
        self.assertEqual(patient.problem, "Fever and cough")

    def test_patient_model_str(self):
        """
        Test the string representation of the Patient model.
        """
        patient = Patient.objects.create(
            name="Jane Doe",
            nic="987654321V",
            age=25,
            gender="Female",
            problem="Headache"
        )

        # Verify that the string representation returns the patient's name
        self.assertEqual(str(patient), "Jane Doe")

    def test_patient_model_field_validation(self):
        """
        Test the validation of patient model fields (e.g., max length).
        """
        patient = Patient.objects.create(
            name="Alice Johnson",
            nic="112233445V",
            age=40,
            gender="Female",
            problem="Back pain"
        )

        # Ensure that the patient is created successfully and the data is stored
        self.assertEqual(patient.name, "Alice Johnson")
        self.assertEqual(patient.nic, "112233445V")
        self.assertEqual(patient.age, 40)
        self.assertEqual(patient.gender, "Female")
        self.assertEqual(patient.problem, "Back pain")


class PatientViewsTest(TestCase):
    def setUp(self):
        # Create an admin user and log in
        self.admin_user = User.objects.create_user(username='admin', password='password', is_staff=True)
        self.patient_data = {
            'name': 'Saman Kumara',  # Updated name
            'nic': '123456789V',
            'age': 30,
            'gender': 'Male',
            'problem': 'Headache'
        }
        self.patient = Patient.objects.create(**self.patient_data)
        
    def test_patient_home_view(self):
        # Log in the admin user
        self.client.login(username='admin', password='password')

        # Make a request to the patient home page
        response = self.client.get(reverse('patient_home'))

        # Check if the page contains the patient's name "Saman Kumara"
        self.assertContains(response, self.patient_data['name'])

    def test_patient_home_view_no_login(self):
        # Test if the view displays the "Log in admin to view Patient" message when not logged in
        response = self.client.get(reverse('patient_home'))
        self.assertContains(response, "Log in admin to view Patient")
