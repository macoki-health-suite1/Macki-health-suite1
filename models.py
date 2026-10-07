from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    ROLES = [
        ("admin", "Administrator"),
        ("doctor", "Doctor"),
        ("nurse", "Nurse / CHEW"),
        ("pharmacist", "Pharmacist"),
        ("lab", "Laboratory Staff"),
        ("records", "Records Officer"),
    ]
    organisation = models.ForeignKey(
        "organisations.Organisation", null=True, blank=True,
        on_delete=models.PROTECT, related_name="users",
    )
    facility = models.ForeignKey(
        "organisations.Facility", null=True, blank=True,
        on_delete=models.SET_NULL, related_name="users",
    )
    role = models.CharField(max_length=20, choices=ROLES, default="nurse")
