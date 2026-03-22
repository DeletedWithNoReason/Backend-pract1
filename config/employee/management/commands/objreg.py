from django.core.management.base import BaseCommand
from django.core.exceptions import ValidationError
import getpass
from employee.models import Employee

class Command(BaseCommand):
    help = 'Registers a new Foundation Operator (Employee)'

    def handle(self, *args, **options):
        self.stdout.write("--- R.O.C.S. OPERATOR REGISTRATION PROTOCOL ---")
        while True:
            eid = input("ENTER EMPLOYEE ID (8 chars): ").upper()
            if len(eid) == 8:
                break
            self.stderr.write(self.style.ERROR("PROTOCOL ERROR: ID MUST BE EXACTLY 8 CHARACTERS."))

        fname = input("FIRST NAME: ")
        lname = input("LAST NAME: ")
        while True:
            key = getpass.getpass("ENTER 5-DIGIT ACCESS KEY: ").upper()
            if len(key) != 5:
                self.stderr.write(self.style.ERROR("PROTOCOL ERROR: KEY MUST BE EXACTLY 5 CHARACTERS."))
                continue

            key_confirm = getpass.getpass("CONFIRM ACCESS KEY: ").upper()
            if key == key_confirm:
                break

            self.stderr.write(self.style.ERROR("ERROR: KEYS DO NOT MATCH."))

        try:
            Employee.objects.create_superuser(
                employee_id=eid,
                password=key,
                first_name=fname,
                last_name=lname
            )
            self.stdout.write(self.style.SUCCESS(f"SUCCESS: OPERATOR [{eid}] REGISTERED IN SYSTEM."))

        except ValidationError as e:
            message = e.messages[0] if hasattr(e, 'messages') else str(e)
            self.stderr.write(self.style.ERROR(f"PROTOCOL VIOLATION: {message}"))

        except Exception as e:
            self.stderr.write(self.style.ERROR(f"CRITICAL SYSTEM ERROR: {e}"))