from django.contrib import admin
from django import forms
from .models import Employee

class EmployeeAdminForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        widgets = {
            'employee_key': forms.PasswordInput(render_value=True),
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            if 'password' in self.fields:
                self.fields['password'].label = "Employee Access Key"
                self.fields['password'].help_text = "Internal system hash generated from the Access Key."

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):

    list_display = ('employee_id', 'last_name', 'first_name', 'employee_key', 'is_staff', 'is_active')
    
    fieldsets = (
        ("Personal Identification", {'fields': ('employee_id', 'first_name', 'last_name')}),
        ("Security Access", {'fields': ('employee_key', 'password')}),
        ("Permissions", {'fields': ('is_staff', 'is_superuser', 'is_active')}),
    )

    readonly_fields = ('password',)
