import os

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    "eversteadinvest.settings"
)

import django
django.setup()

from django.contrib.auth import get_user_model
from django.core.management import call_command

User = get_user_model()

username = os.getenv(
    f"DJANGO_SUPERUSER_{User.USERNAME_FIELD.upper()}"
)

if not username:
    raise ValueError(
        f"Missing environment variable: "
        f"DJANGO_SUPERUSER_{User.USERNAME_FIELD.upper()}"
    )

if User.objects.filter(**{User.USERNAME_FIELD: username}).exists():
    print("Superuser already exists. No changes made.")
else:
    print("Creating Django superuser...")
    call_command("createsuperuser", interactive=False)
    print("Superuser created successfully!")
