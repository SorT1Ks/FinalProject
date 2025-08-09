from django import forms

class LoanForm(forms.Form):
    Gender = forms.ChoiceField(
        label="Стать заявника",
        choices=[
            ('Male', 'Чоловік'),
            ('Female', 'Жінка')
        ],
        required=True
    )
    Married = forms.ChoiceField(
        label="Сімейний стан",
        choices=[
            ('No', 'Не одружений/Не заміжня'),
            ('Yes', 'Одружений/Заміжня')
        ],
        required=True
    )
    Dependents = forms.ChoiceField(
        label="Кількість утриманців",
        choices=[
            ('0', '0'),
            ('1', '1'),
            ('2', '2'),
            ('3+', '3 або більше')
        ],
        required=True
    )
    Education = forms.ChoiceField(
        label="Освіта",
        choices=[
            ('Graduate', 'Вища'),
            ('Not Graduate', 'Середня/Початкова')
        ],
        required=True
    )
    Self_Employed = forms.ChoiceField(
        label="Самозайнятість",
        choices=[
            ('No', 'Ні'),
            ('Yes', 'Так')
        ],
        required=True
    )
    ApplicantIncome = forms.FloatField(
        label="Місячний дохід заявника (грн)",
        min_value=0,
        required=True
    )
    CoapplicantIncome = forms.FloatField(
        label="Місячний дохід співзаявника (грн)",
        min_value=0,
        required=True
    )
    LoanAmount = forms.FloatField(
        label="Бажана сума кредиту (тис. грн)",
        min_value=0,
        required=True
    )
    Loan_Amount_Term = forms.FloatField(
        label="Бажаний термін кредиту (місяців)",
        min_value=1,
        required=True
    )
    Credit_History = forms.ChoiceField(
        label="Наявність позитивної кредитної історії",
        choices=[
            ('1', 'Так, є позитивна історія'),
            ('0', 'Ні, немає позитивної історії')
        ],
        required=True
    )
    Property_Area = forms.ChoiceField(
        label="Тип місця проживання",
        choices=[
            ('Urban', 'Місто'),
            ('Semiurban', 'Передмістя'),
            ('Rural', 'Село')
        ],
        required=True
    )