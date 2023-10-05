from django.db import models
from django.conf import settings


GENDER_CHOICES = (
    ('Masculino', 'Masculino'),
    ('Femenino', 'Femenino'),
)


class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE)
    date_of_birth = models.DateField(
        blank=True,
        null=True)
    photo = models.ImageField(
        upload_to='users/%Y/%m/%d/',
        blank=True)
    gender = models.CharField(
        null=True,
        blank=True,
        choices=GENDER_CHOICES,
        max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Profile of {self.user.username}'
