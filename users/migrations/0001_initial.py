# Generated by Django 3.0.4 on 2021-01-02 13:01

import django.core.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='reservations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=50)),
                ('contact_number', models.CharField(max_length=13, validators=[django.core.validators.RegexValidator(message='Phone number must be +251 ** or 09 ** format upto 13 digit.', regex='^\\+?(251)?\\d{10,13}$')])),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('No_ofperson', models.CharField(max_length=10)),
                ('preferred_item', models.CharField(choices=[('1', 'humanhair'), ('2', 'bridalcloths'), ('3', 'makeup')], max_length=5)),
                ('occasion', models.CharField(choices=[('1', 'Wedding'), ('2', 'birthday'), ('3', 'Anniversary')], max_length=5)),
            ],
        ),
    ]
