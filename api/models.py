import uuid
from django.db import models
from django.utils import timezone

class Member(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    receipt = models.CharField(max_length=50)
    purchase_date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.email
