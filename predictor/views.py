from django.shortcuts import render
from .forms import LoanForm
import joblib
import numpy as np
import pandas as pd
import os

MODEL_PATH = os.path.join(os.path.dirname(__file__), '..', 'ml', 'model.pkl')

def predict_loan_status(input_data):
    columns = [
        'Gender',
        'Married',
        'Dependents',
        'Education',
        'Self_Employed',
        'ApplicantIncome',
        'CoapplicantIncome',
        'LoanAmount',
        'Loan_Amount_Term',
        'Credit_History',
        'Property_Area'
    ]
    print("DEBUG: input_data:", input_data)
    print("DEBUG: types:", [type(x) for x in input_data])
    df = pd.DataFrame([input_data], columns=columns)
    print("DEBUG: DataFrame dtypes:\n", df.dtypes)
    print("DEBUG: DataFrame values:\n", df)
    model = joblib.load(MODEL_PATH)
    prediction = model.predict(df)
    print("DEBUG: prediction result:", prediction)
    return prediction[0]

def loan_form_view(request):
    if request.method == 'POST':
        form = LoanForm(request.POST)
        if form.is_valid():
            print("DEBUG: cleaned_data from form:", form.cleaned_data)
            def safe_float(val, default=0.0):
                try:
                    return float(val)
                except (TypeError, ValueError):
                    return default

            def safe_int(val, default=0):
                try:
                    return int(val)
                except (TypeError, ValueError):
                    return default

            data = [
                form.cleaned_data['Gender'],
                form.cleaned_data['Married'],
                form.cleaned_data['Dependents'],
                form.cleaned_data['Education'],
                form.cleaned_data['Self_Employed'],
                float(form.cleaned_data['ApplicantIncome']),
                float(form.cleaned_data['CoapplicantIncome']),
                float(form.cleaned_data['LoanAmount']),
                float(form.cleaned_data['Loan_Amount_Term']),
                float(form.cleaned_data['Credit_History']),
                form.cleaned_data['Property_Area']
            ]
            print("DEBUG: Data for prediction:", data)
            result = predict_loan_status(data)
            print("DEBUG: model result (raw):", result)
            result_text = 'Схвалено ✅' if result == 'Y' else 'Відмовлено ❌'
            return render(request, 'predictor/result.html', {'result': result_text})
    else:
        form = LoanForm()
    return render(request, 'predictor/form.html', {'form': form})