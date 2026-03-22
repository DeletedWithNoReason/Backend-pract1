from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.core.validators import RegexValidator

class EmployeeManager(BaseUserManager):
    def create_user(self, employee_id, password=None, **extra_fields):
        if not employee_id:
            raise ValueError('The Employee ID must be set')
        
        key = extra_fields.pop('employee_key', password)

        user = self.model(
            employee_id=employee_id,
            employee_key=key,
            **extra_fields
        )
        
        if password:
            user.set_password(password)
        elif key:
            user.set_password(key)
            
        user.save(using=self._db)
        return user

    def create_superuser(self, employee_id, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(employee_id, password, **extra_fields)

class Employee(AbstractUser):
    username = None 

    password = models.CharField(max_length=128, verbose_name="Access Key Hash")
    
    id_validator = RegexValidator(
        regex=r'^[A-Z0-9]{8}$',
        message='Employee ID must be exactly 8 characters (uppercase letters and digits).'
    )

    key_validator = RegexValidator(
        regex=r'^[A-Z0-9]{5}$',
        message='Access Key must be exactly 5 characters (uppercase letters and digits).'
    )

    employee_id = models.CharField(
        max_length=8, 
        unique=True, 
        validators=[id_validator],
        verbose_name="Employee ID"
    )
    
    employee_key = models.CharField(
        max_length=5, 
        unique=True, 
        validators=[key_validator],
        verbose_name="Access Key"
    )

    USERNAME_FIELD = 'employee_id'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = EmployeeManager()

    def __str__(self):
        return f"{self.first_name} {self.last_name} [{self.employee_id}]"
    
    def save(self, *args, **kwargs):

        if self.employee_id:
            self.employee_id = self.employee_id.upper()

        if self.employee_key:
            self.employee_key = self.employee_key.upper()
            self.set_password(self.employee_key)

        self.full_clean()

        super().save(*args, **kwargs)