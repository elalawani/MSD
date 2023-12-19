import uuid
from django.db import models
from datetime import date
from account.models import User


class Patient(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    OTHER = 'O'
    GENDER_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (OTHER, 'Other'),
    ]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    street = models.CharField(max_length=200)
    house_number = models.CharField(max_length=3)
    postal_code = models.CharField(max_length=5)
    city = models.CharField(max_length=200)
    date_of_birth = models.DateField(verbose_name="Date of Birth")
    email = models.EmailField(unique=True, null=True)
    phone = models.CharField(max_length=12)
    doctors = models.ManyToManyField(User,
                                     related_name='doctor_patient',
                                     limit_choices_to={'role': User.DOCTOR}, blank=True)
    nurses = models.ManyToManyField(User,
                                    related_name='nurse_patient',
                                    limit_choices_to={'role': User.NURSE}, blank=True)
    reason_of_visiting = models.TextField(blank=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def age(self):
        today = date.today()
        return today.year - self.date_of_birth.year - (
                    (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day))

    def __str__(self):
        return self.first_name
