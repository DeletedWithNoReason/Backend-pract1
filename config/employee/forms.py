from django import forms

class EmployeeLoginForm(forms.Form):
    employee_id = forms.CharField(
        max_length=8,
        widget=forms.TextInput(attrs={
            'placeholder': 'EMPLOYEE ID',
            'style': 'text-transform: uppercase;',
            'autocomplete': 'off',
            'class': 'terminal-input'
        })
    )
    access_key = forms.CharField(
        max_length=5,
        widget=forms.PasswordInput(attrs={
            'placeholder': 'ACCESS KEY',
            'class': 'terminal-input'
        })
    )