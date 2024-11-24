from django.test import TestCase, Client
from django.urls import reverse
from patient.models import Patient
from medicine.models import Medicine
from datetime import date
from transaction.models import Transaction

# Create your tests here.


class TransactionModelTest(TestCase):
    def setUp(self):
        # Create test patient and medicine objects
        self.patient = Patient.objects.create(
            name='Saman Kumara',
            nic='123456789V',
            age=30,
            gender='Male',
            problem='Headache'
        )
        self.medicine = Medicine.objects.create(
            name='Paracetamol',
            description='Pain reliever',
            price=100.00,  # Assuming you have a price field in the Medicine model
            stock=100,
            mfg_date=date(2022, 1, 1),
            expiry_date=date(2025, 12, 31),
        )

    def test_create_transaction(self):
        # Create a new transaction
        transaction = Transaction.objects.create(
            patient=self.patient,
            medicine=self.medicine,
            quantity=2,
            total=200.00  # price * quantity
        )

        # Fetch the transaction from the database
        transaction = Transaction.objects.get(id=transaction.id)

        # Check if the transaction was created correctly
        self.assertEqual(transaction.patient.name, 'Saman Kumara')
        self.assertEqual(transaction.medicine.name, 'Paracetamol')
        self.assertEqual(transaction.quantity, 2)
        self.assertEqual(transaction.total, 200.00)

    def test_transaction_str_method(self):
        # Create a transaction
        transaction = Transaction.objects.create(
            patient=self.patient,
            medicine=self.medicine,
            quantity=1,
            total=100.00
        )

        # Check if the string representation of the transaction is correct
        self.assertEqual(str(transaction), 'Transaction for Saman Kumara - Paracetamol (Quantity: 1)')

    def test_transaction_model_relations(self):
        # Create a new transaction
        transaction = Transaction.objects.create(
            patient=self.patient,
            medicine=self.medicine,
            quantity=3,
            total=300.00
        )

        # Test if the patient and medicine relations work
        self.assertEqual(transaction.patient, self.patient)
        self.assertEqual(transaction.medicine, self.medicine)

    def test_total_calculation(self):
        # Calculate the total based on quantity and medicine price
        transaction = Transaction.objects.create(
            patient=self.patient,
            medicine=self.medicine,
            quantity=5,
            total=500.00  # Assuming the price of medicine is 100
        )

        # Test if the total is calculated correctly
        self.assertEqual(transaction.total, self.medicine.price * transaction.quantity)


class AddTransactionViewTests(TestCase):

    def setUp(self):
        self.client = Client()
        # Create sample Patient and Medicine objects
        self.patient = Patient.objects.create(name="Test Patient", age=30)
        self.medicine = Medicine.objects.create(name="Test Medicine", price=50.0)
        self.add_transaction_url = reverse('add_transaction')  # Adjust if your URL name is different
        self.success_url = reverse('transaction_success')

    

class TransactionSuccessViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.success_url = reverse('transaction_success')

    def test_transaction_success_view(self):
        # Test the success view
        response = self.client.get(self.success_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'transaction/success.html')

class ViewTransactionsTests(TestCase):
    def setUp(self):
        self.client = Client()
        # Create sample Patient, Medicine, and Transactions
        self.patient = Patient.objects.create(name="Test Patient", age=30)
        self.medicine = Medicine.objects.create(name="Test Medicine", price=50.0)
        self.transaction = Transaction.objects.create(
            patient=self.patient,
            medicine=self.medicine,
            quantity=2,
            total=100.0
        )
        self.view_transactions_url = reverse('view_transactions')

  