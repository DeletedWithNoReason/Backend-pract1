from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import ValidationError
from .forms import EmployeeLoginForm
from .models import Employee

def login_view(request):
    error_message = None
    if request.method == 'POST':
        form = EmployeeLoginForm(request.POST)
        if form.is_valid():
            eid = form.cleaned_data['employee_id'].upper()
            key = form.cleaned_data['access_key'].upper()
            
            try:
                temp_user = Employee(employee_id=eid, employee_key=key)
                temp_user.full_clean(
                    exclude=['password', 'last_login', 'date_joined'], 
                    validate_unique=False
                )
                user = authenticate(request, username=eid, password=key)
                
                if user is not None:
                    login(request, user)
                    return redirect('hubs_list') 
                else:
                    error_message = "TERMINAL_ERROR: INVALID_CREDENTIALS"
            
            except ValidationError:
                error_message = f"PROTOCOL_VIOLATION: INVALID_DATA_STRUCTURE"
            
            except Exception:
                error_message = f"CRITICAL_SYSTEM_ERROR: ACCESS_ABORTED"
    else:
        form = EmployeeLoginForm()
        
    return render(request, 'employee/login.html', {
        'form': form, 
        'error_message': error_message
    })

def logout_view(request):
    logout(request)
    return redirect('login')