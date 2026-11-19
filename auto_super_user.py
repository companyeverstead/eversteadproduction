
import os

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    "eversteadinvest.settings"
)

import django
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

username = os.getenv(
    f"DJANGO_SUPERUSER_{User.USERNAME_FIELD.upper()}"
)

password = os.getenv("DJANGO_SUPERUSER_PASSWORD")

if not username:
    raise ValueError("Superuser username is missing!")

if not password:
    raise ValueError("Superuser password is missing!")

user_data = {
    User.USERNAME_FIELD: username
}

for field in User.REQUIRED_FIELDS:
    value = os.getenv(
        f"DJANGO_SUPERUSER_{field.upper()}"
    )

    if not value:
        raise ValueError(
            f"Missing environment variable: "
            f"DJANGO_SUPERUSER_{field.upper()}"
        )

    user_data[field] = value

if User.objects.filter(
    **{User.USERNAME_FIELD: username}
).exists():

    print("Superuser already exists. No changes made.")

else:
    User.objects.create_superuser(
        **user_data,
        password=password
    )

    print("Superuser created successfully!")
