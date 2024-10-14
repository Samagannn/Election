from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from account.models import User
from django.utils import timezone


class Candidate(models.Model):
    name = models.CharField(max_length=100)
    committee = models.CharField(max_length=100)
    fractions = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='photos/')
    phone_number = PhoneNumberField(unique=True)
    email = models.EmailField(unique=True)
    bio = models.TextField(max_length=100)

    def __str__(self):
        return self.name


class Voter(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.address


class MyVotes(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)

    def __str__(self):
        return self.candidate.name


class Appeal(models.Model):
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = PhoneNumberField(unique=True)
    region_or_city = models.CharField(max_length=100)
    address_type = models.CharField(max_length=100)
    address_name = models.CharField(max_length=100)
    house_number = models.CharField(max_length=100)
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    text_of_the_appeal = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.last_name


class MyAppeal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    appeal = models.ForeignKey(Appeal, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Appeal by {self.user}"
# Create your models here.
