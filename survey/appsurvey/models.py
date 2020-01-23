from django.db import models
from django.utils import timezone

# Create your models here.

RESTRICTION_CHOICES = (
    ('Reasonable', 'Reasonable'),
    ('Too Restrictive', 'Too Restrictive'),
)

JEANS_CHOICES = (
    ('Yes', 'Yes'),
    ('No', 'No'),
)

DRESSSHORT_CHOICES = (
    ('Yes', 'Yes'),
    ('No', 'No'),
)

ATTEND_CHOICES = (
    ('Yes', 'Yes'),
    ('No', 'No'),
)

class Survey(models.Model):
    email = models.EmailField(blank = True)
    restriction = models.CharField(max_length = 65, choices = RESTRICTION_CHOICES)
    jeans = models.CharField(max_length = 65, choices = JEANS_CHOICES)
    dressshort = models.CharField(max_length = 65, choices = DRESSSHORT_CHOICES)
    attend = models.CharField(max_length = 65, choices = ATTEND_CHOICES)
    date = models.DateTimeField(default = timezone.now())

    def __str__(self):
        return self.restriction
