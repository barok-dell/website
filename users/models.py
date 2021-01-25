from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator
class reservations(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    contact_number_regex = RegexValidator(
        regex='^\+?(251)?\d{10,13}$',
        message='Phone number must be +251 ** or 09 ** format upto 13 digit.')
    contact_number = models.CharField(max_length=13, validators=[contact_number_regex])
    date = models.DateTimeField(default=timezone.now)
    No_ofperson = models.CharField(max_length=10)
    PREFERRED_ITEM = (
        ('1', 'humanhair'), ('2', 'bridalcloths'), ('3', 'makeup'))
    preferred_item = models.CharField(max_length=5, choices=PREFERRED_ITEM)
    OCCASION = (
        ('1', 'Wedding'), ('2', 'birthday'), ('3', 'Anniversary'))
    occasion = models.CharField(max_length=5, choices=OCCASION)


# Create your models here.