# Generated by Django 3.1.4 on 2021-10-13 21:36

import accounts.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='accounts.customuser', verbose_name='Email')),
                ('fullAddress', models.CharField(max_length=1024, verbose_name='Full address')),
                ('address1', models.CharField(help_text='Street address, P.O. box, company, name, c/o', max_length=1024, verbose_name='Address line 1')),
                ('address2', models.CharField(blank=True, help_text='Appartment, suite, unit building, floor, etc.', max_length=1024, null=True, verbose_name='Address line 2')),
                ('zip_code', models.CharField(max_length=12, verbose_name='ZIP / Postal code')),
                ('city', models.CharField(max_length=1024, verbose_name='City')),
                ('country', accounts.models.CountryField(verbose_name='Country')),
            ],
            options={
                'verbose_name_plural': 'Addresses',
            },
        ),
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='accounts.customuser', verbose_name='Email')),
                ('site', models.URLField(blank=True)),
                ('birthday', models.DateField(default=django.utils.timezone.now)),
                ('place_of_birth', models.CharField(default='Kalisz', max_length=100, verbose_name='Place Of Birth')),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(blank=True, help_text="Phone number ex: '+41524204242'", max_length=128, region=None)),
                ('cellphone_number', phonenumber_field.modelfields.PhoneNumberField(blank=True, help_text="Phone number ex: '+41524204242'", max_length=128, region=None)),
                ('nationality', accounts.models.CountryField(verbose_name='Nationality')),
            ],
        ),
    ]
