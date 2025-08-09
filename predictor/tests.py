from django.test import TestCase, Client
from django.urls import reverse

class LoanFormTest(TestCase):
    def test_form_valid(self):
        data = {
            'Gender': 0,
            'Married': 1,
            'Dependents': 0,
            'Education': 0,
            'Self_Employed': 0,
            'ApplicantIncome': 3000,
            'CoapplicantIncome': 0,
            'LoanAmount': 100,
            'Loan_Amount_Term': 360,
            'Credit_History': 1.0,
            'Property_Area': 0,
        }
        response = self.client.post(reverse('loan_form'), data)
        self.assertContains(response, "Loan Application Result")