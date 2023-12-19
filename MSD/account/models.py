from django.utils import timezone
import uuid
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.db import models


class CustomUserManager(UserManager):
    def _create_user(self, username, email, password, **extra_fields):
        if not email:
            raise ValueError("Email Address is not valid")

        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_user(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, email, password, **extra_fields)

    def create_superuser(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(username, email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    DOCTOR = 'DR'
    NURSE = 'NR'
    STAFF = 'ST'
    ROLE_CHOICES = [
        (DOCTOR, 'Doctor'),
        (NURSE, 'Nurse'),
        (STAFF, 'Staff'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(unique=True, max_length=255)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=225, blank=True, default='')
    last_name = models.CharField(max_length=225, blank=True, default='')
    avatar = models.ImageField(upload_to='avatars', blank=True, null=True)
    role = models.CharField(max_length=2, choices=ROLE_CHOICES, default=STAFF, blank=True, null=True)

    MALE = 'M'
    FEMALE = 'F'
    OTHER = 'O'

    GENDER_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (OTHER, 'Other'),
    ]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True, null=True)
    street = models.CharField(max_length=200, blank=True, null=True)
    nr = models.CharField(max_length=3, blank=True, null=True)
    PLZ = models.CharField(max_length=5, blank=True, null=True)
    city = models.CharField(max_length=200, blank=True, null=True)

    is_active = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(blank=True, null=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
