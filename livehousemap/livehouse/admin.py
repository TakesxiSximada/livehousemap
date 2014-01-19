from django.contrib import admin
from .models import (
    House,
    Landmark,
    )

for cls in (House, Landmark):
    admin.site.register(cls)
