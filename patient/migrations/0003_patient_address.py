# Generated by Django 5.1.3 on 2024-11-23 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0002_alter_patient_age_alter_patient_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='address',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
